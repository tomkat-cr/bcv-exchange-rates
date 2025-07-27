# utilities.py
# 2025-05-14 | CR

import datetime
import warnings


def get_default_response():
    apiResponse = dict()
    apiResponse['error'] = False
    apiResponse['error_message'] = []
    apiResponse['data'] = dict()
    return apiResponse


def get_formatted_date():
    date_format = "%Y-%m-%d %H:%M:%S UTC"
    formatted_date = datetime.date.strftime(
        datetime.datetime.now(datetime.timezone.utc), date_format
    )
    return formatted_date


def convert_spanish_date(date_str):
    """
    Converts a Spanish date string in the format "Día, DD Mes AAAA"
    to "YYYY-MM-DD".

    Args:
        date_str (str): The date string in Spanish format.
                        e.g., "Lunes, 21 Julio 2025".

    Returns:
        str: The date string in "YYYY-MM-DD" format.
    """
    if not date_str or not isinstance(date_str, str):
        return None

    parts = date_str.split()
    if len(parts) < 4:
        return None

    day = parts[1]
    month_str = parts[2]
    year = parts[3]

    spanish_months = {
        'enero': '01',
        'febrero': '02',
        'marzo': '03',
        'abril': '04',
        'mayo': '05',
        'junio': '06',
        'julio': '07',
        'agosto': '08',
        'septiembre': '09',
        'octubre': '10',
        'noviembre': '11',
        'diciembre': '12',
    }

    month = spanish_months.get(month_str.lower())

    if not month:
        return None

    try:
        # Format the date parts into YYYY-MM-DD
        formatted_date = f"{year}-{month}-{int(day):02d}"
        # Validate the date
        datetime.datetime.strptime(formatted_date, '%Y-%m-%d')
        return formatted_date
    except (ValueError, TypeError):
        return None


def fix_value(value):
    try:
        value = value.replace(",", ".")
        return float(value)
    except (ValueError, AttributeError) as e:
        warnings.warn(f"Invalid value encountered in fix_value: {value}."
                      f" Error: {e}")
        return None
