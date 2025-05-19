# get_bcv_exchange_rates.py
# 2023-01-05 | CR

import warnings
from bs4 import BeautifulSoup
import requests

from utilities import get_formatted_date


def fix_value(value):
    value = value.replace(",", ".")
    return float(value)


def get_currency_section_value(soup, apiResponse, currency):
    error_message = []
    error_flag = False
    exchange_value = None
    currency_symbol = None
    # Locate the element with id "dolar" (or "rubro" or "euro")
    try:
        currencySection = soup.find("div", {"id": currency})
    except Exception as err:
        error_flag = True
        error_message = f'id "{currency}" not found | {str(err)}'
    # Scrape the first <div> inside it
    if not error_flag:
        try:
            firstDiv = currencySection.find("div")
        except Exception as err:
            error_flag = True
            error_message = f'1st <div> not found | {str(err)}'
    # Scrape the second <div> inside that first <div>
    if not error_flag:
        try:
            secondDiv = firstDiv.find("div")
        except Exception as err:
            error_flag = True
            error_message = f'2nd <div> not found | {str(err)}'
    # Scrape the <strong> element, get the text attribute
    if not error_flag:
        try:
            exchange_value = secondDiv.find("strong").text.strip()
        except Exception as err:
            error_flag = True
            error_message = f'The <strong> in 2nd <div> not found | {str(err)}'
    # Scrape the <span> element, get the text attribute
    if not error_flag:
        exchange_value = fix_value(exchange_value)
        try:
            currency_symbol = secondDiv.find("span").text.strip()
        except Exception as err:
            error_flag = True
            error_message = f'The <span> in 2nd <div> not found | {str(err)}'

    apiResponse['data'][currency] = dict()
    apiResponse['data'][currency]['symbol'] = currency_symbol
    apiResponse['data'][currency]['value'] = exchange_value

    if error_flag:
        apiResponse['error'] = True
        apiResponse['error_message'].append(
            f'ERROR(s) on id "{currency}"'
        )
        apiResponse['data'][currency]['error_message'] = error_message


def get_bcv_exchange_rates():

    apiResponse = dict()
    apiResponse['error'] = False
    apiResponse['error_message'] = []
    apiResponse['data'] = dict()

    url = "https://www.bcv.org.ve"

    try:
        response = requests.get(url=url)
    except requests.exceptions.SSLError:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(url=url, verify=False)
        except Exception as err:
            apiResponse['error'] = True
            apiResponse['error_message'].append(str(err))
    except Exception as err:
        apiResponse['error'] = True
        apiResponse['error_message'].append(str(err))

    if apiResponse['error']:
        return apiResponse

    soup = BeautifulSoup(response.text, "html.parser")

    get_currency_section_value(soup, apiResponse, "euro")
    get_currency_section_value(soup, apiResponse, "yuan")
    get_currency_section_value(soup, apiResponse, "lira")
    get_currency_section_value(soup, apiResponse, "rublo")
    get_currency_section_value(soup, apiResponse, "dolar")

    # Locate the <span> element with class "date-display-single".
    # get the text attribute
    effective_date = None
    try:
        effective_date = soup.find(
            "span", {"class": "date-display-single"}
        ).text.strip()
    except Exception as err:
        apiResponse['error'] = True
        apiResponse['error_message'].append(
            'The "span" with "class": "date-display-single" to get' +
            f' the effective_date value not found | {str(err)}'
        )

    apiResponse['data']['effective_date'] = effective_date
    apiResponse['data']['run_timestamp'] = get_formatted_date()

    return apiResponse
