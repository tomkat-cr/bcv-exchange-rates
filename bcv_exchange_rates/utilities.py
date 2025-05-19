# utilities.py
# 2025-05-14 | CR

import datetime


def get_formatted_date():
    date_format = "%Y-%m-%d %H:%M:%S UTC"
    formatted_date = datetime.date.strftime(
        datetime.datetime.now(datetime.timezone.utc), date_format
    )
    return formatted_date


def get_default_response():
    apiResponse = dict()
    apiResponse['error'] = False
    apiResponse['error_message'] = []
    apiResponse['data'] = dict()
    return apiResponse
