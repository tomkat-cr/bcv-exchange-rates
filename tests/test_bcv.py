import unittest
import warnings
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
from bcv_exchange_rates.bcv import (
    convert_spanish_date, fix_value, get_currency_section_value,
    get_bcv_exchange_rates
)


class TestBCV(unittest.TestCase):

    def test_fix_value(self):
        self.assertEqual(fix_value("1,23"), 1.23)
        self.assertEqual(fix_value("1.23"), 1.23)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertIsNone(fix_value("abc"))
            self.assertIsNone(fix_value(None))

    def test_convert_spanish_date(self):
        self.assertEqual(convert_spanish_date(
            "Lunes, 21 Julio 2025"), "2025-07-21")
        self.assertEqual(convert_spanish_date(
            "Martes, 1 Enero 2024"), "2024-01-01")
        self.assertIsNone(convert_spanish_date("Lunes, 21 XYZ 2025"))
        self.assertIsNone(convert_spanish_date("Invalid Date"))
        self.assertIsNone(convert_spanish_date(None))
        self.assertIsNone(convert_spanish_date(""))

    def test_get_currency_section_value_success(self):
        html_content = '''
        <div id="dolar">
            <div>
                <div>
                    <strong>1,23</strong>
                    <span>USD</span>
                </div>
            </div>
        </div>
        '''
        soup = BeautifulSoup(html_content, 'html.parser')
        api_response = {'data': {}, 'error': False, 'error_message': []}
        get_currency_section_value(soup, api_response, 'dolar')

        self.assertFalse(api_response['error'])
        self.assertEqual(api_response['data']['dolar']['value'], 1.23)
        self.assertEqual(api_response['data']['dolar']['symbol'], 'USD')

    def test_get_currency_section_value_failure(self):
        html_content = '<div id="dolar"></div>'
        soup = BeautifulSoup(html_content, 'html.parser')
        api_response = {'data': {}, 'error': False, 'error_message': []}
        get_currency_section_value(soup, api_response, 'dolar')

        self.assertTrue(api_response['data']['dolar']['error'])
        self.assertIn('Required tags not found',
                      api_response['data']['dolar']['error_message'])

    @patch('requests.get')
    def test_get_bcv_exchange_rates_success(self, mock_get):
        mock_response = Mock()
        mock_response.text = '''
        <html>
            <body>
                <div id="dolar">
                    <div>
                        <div>
                            <strong>1,23</strong>
                            <span>USD</span>
                        </div>
                    </div>
                </div>
                <div id="euro">
                    <div>
                        <div>
                            <strong>2,34</strong>
                            <span>EUR</span>
                        </div>
                    </div>
                </div>
                <div id="yuan"></div>
                <div id="lira"></div>
                <div id="rublo"></div>
                <span class="date-display-single">Lunes, 21 Julio 2025</span>
            </body>
        </html>
        '''
        mock_get.return_value = mock_response

        api_response = get_bcv_exchange_rates()

        self.assertFalse(api_response['error'])
        self.assertEqual(api_response['data']['dolar']['value'], 1.23)
        self.assertEqual(api_response['data']['euro']['value'], 2.34)
        self.assertEqual(api_response['data']['effective_date'],
                         'Lunes, 21 Julio 2025')
        self.assertEqual(api_response['data']['effective_date_ymd'],
                         '2025-07-21')

    @patch('requests.get', side_effect=Exception('Test Error'))
    def test_get_bcv_exchange_rates_request_failure(self, mock_get):
        api_response = get_bcv_exchange_rates()

        self.assertTrue(api_response['error'])
        self.assertIn('Test Error', api_response['error_message'])


if __name__ == '__main__':
    unittest.main()
