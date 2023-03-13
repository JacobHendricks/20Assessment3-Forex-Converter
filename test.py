from unittest import TestCase
from app import app
from currency import *


app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ForexTestCase(TestCase):
    """testing Flask app"""

    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<H1>Currency Converter</H1>', html)

    def test_home_form(self):
        with app.test_client() as client:
            resp = client.post(
                '/result', data={"conv-from": "USD", "conv-to": "EUR", "amount": 1})
            html = resp.get_data(as_text=True)

            # self.assertEqual(resp.status_code, 200)
            # self.assertIn(
            #     '<p class="result"> Converted Amount = 0.93</p>', html)

    # def :
    #     with self.client:
    #         response = self.client.get('/')

    def test_redirection(self):
        with app.test_client() as client:
            resp = client.get("/convert")

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/")

    def test_convert(self):
        self.assertEqual(convert("USD", "EUR", 1), 0.93)
