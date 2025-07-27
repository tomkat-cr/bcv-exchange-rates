# get_bcv_exchange_rates.py
# 2023-01-05 | CR
from bs4 import BeautifulSoup
import requests
import warnings

from bcv_exchange_rates.utilities import (
    get_formatted_date,
    fix_value,
    convert_spanish_date,
)

DEFAULT_TIMEOUT = 10    # seconds
ALTERNATIVE_VERIFY = False  # False to ignore SSL errors


def get_currency_section_value(soup, apiResponse, currency):
    apiResponse['data'][currency] = {
        'symbol': None,
        'value': None,
        'error': False,
        'error_message': None
    }

    currency_section = soup.find("div", {"id": currency})
    if not currency_section:
        apiResponse['data'][currency]['error'] = True
        apiResponse['data'][currency]['error_message'] = \
            f'id "{currency}" not found'
        return

    try:
        strong_tag = currency_section.find("strong")
        span_tag = currency_section.find("span")

        if strong_tag and span_tag:
            exchange_value = fix_value(strong_tag.text.strip())
            currency_symbol = span_tag.text.strip()

            apiResponse['data'][currency]['symbol'] = currency_symbol
            apiResponse['data'][currency]['value'] = exchange_value
        else:
            raise ValueError("Required tags not found")

    except Exception as err:
        apiResponse['data'][currency]['error'] = True
        apiResponse['data'][currency]['error_message'] = \
            f'Error processing id "{currency}": {str(err)}'


def get_bcv_exchange_rates():

    apiResponse = dict()
    apiResponse['error'] = False
    apiResponse['error_message'] = []
    apiResponse['data'] = dict()

    url = "https://www.bcv.org.ve"

    try:
        response = requests.get(url=url, timeout=DEFAULT_TIMEOUT)
    except requests.exceptions.SSLError:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(
                    url=url,
                    verify=ALTERNATIVE_VERIFY,
                    timeout=DEFAULT_TIMEOUT
                )
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
    effective_date_str = None
    try:
        effective_date_str = soup.find(
            "span", {"class": "date-display-single"}
        ).text.strip()
    except Exception as err:
        apiResponse['error'] = True
        apiResponse['error_message'].append(
            'The "span" with "class": "date-display-single" to get' +
            f' the effective_date value not found | {str(err)}'
        )

    apiResponse['data']['effective_date'] = effective_date_str
    apiResponse['data']['effective_date_ymd'] = \
        convert_spanish_date(effective_date_str)
    apiResponse['data']['run_timestamp'] = get_formatted_date()

    return apiResponse
