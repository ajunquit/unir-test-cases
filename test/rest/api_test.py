import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")
    # ***********************************
    # *** ADD UNIT TEST CASES ***
    # ***********************************
    def test_api_add_return_correct_result(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_return_correct_result(self):
        url = f"{BASE_URL}/calc/add/1/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_return_correct_result_decimals(self):
        url = f"{BASE_URL}/calc/add/2.05/0.99"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_negative(self):
        url = f"{BASE_URL}/calc/add/-1/-3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/add/two/1"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_add_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/add/1/two"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_add_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/add/one/two"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_add_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/add/-six/*--hello++*"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    # ***********************************
    # *** SUBSTRACT UNIT TEST CASES ***
    # ***********************************
    def test_api_substract_return_correct_result(self):
        url = f"{BASE_URL}/calc/substract/2/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract_return_correct_result(self):
        url = f"{BASE_URL}/calc/substract/9.99/-0.25"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract_return_correct_result_negative(self):
        url = f"{BASE_URL}/calc/substract/-2/-8"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract_return_correct_result_decimals(self):
        url = f"{BASE_URL}/calc/substract/10.99/0.88"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/substract/*&455hh/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    # ***********************************
    # *** MULTIPLY UNIT TEST CASES ***
    # ***********************************
    def test_api_multiply_return_correct_result(self):
        url = f"{BASE_URL}/calc/multiply/5/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_return_correct_result(self):
        url = f"{BASE_URL}/calc/multiply/5/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_return_correct_result(self):
        url = f"{BASE_URL}/calc/multiply/10/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_return_correct_result_negative(self):
        url = f"{BASE_URL}/calc/multiply/-4/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_return_correct_result_negative(self):
        url = f"{BASE_URL}/calc/multiply/-10/-15"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_return_correct_result_decimals(self):
        url = f"{BASE_URL}/calc/multiply/2.99/5.88"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_return_correct_result_decimals(self):
        url = f"{BASE_URL}/calc/multiply/-78/-0.52"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/multiply/+**five*+/six"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_multiply_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/multiply/nine/zero"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    # ***********************************
    # *** DIVIDE - API TEST CASES     ***
    # ***********************************

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/18/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/3/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_divide_fail_dividebyzero(self):
        url = f"{BASE_URL}/calc/divide/1/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_divide_fail_anything_divide_byzero(self):
        url = f"{BASE_URL}/calc/divide/*&455hh/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_divide_fail_dividebyzero(self):
        url = f"{BASE_URL}/calc/divide/0/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_divide_fail_dividebyzero(self):
        url = f"{BASE_URL}/calc/divide/2/-0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    # ***********************************
    # *** POWER UNIT TEST CASES ***
    # ***********************************

    def test_api_power_base_positive_exp_positive(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_base_positive_exp_positive(self):
        url = f"{BASE_URL}/calc/power/2/0.05"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_base_positive_exp_zero(self):
        url = f"{BASE_URL}/calc/power/2/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_base_positive_exp_negative(self):
        url = f"{BASE_URL}/calc/power/25/-3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_base_negative_exp_positive(self):
        url = f"{BASE_URL}/calc/power/-7/3.0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_base_negative_exp_negative(self):
        url = f"{BASE_URL}/calc/power/-5.56/-3.33"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/power/five/six"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Error en la peticion {url}"
        )

    # ***********************************
    # *** SQUARE ROOT UNIT TEST CASES ***
    # ***********************************

    def test_api_square_root_positive(self):
        url = f"{BASE_URL}/calc/square_root/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_square_root_decimal(self):
        url = f"{BASE_URL}/calc/square_root/2.25"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_square_root_zero(self):
        url = f"{BASE_URL}/calc/square_root/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_square_root_bignumber(self):
        url = f"{BASE_URL}/calc/square_root/999999999"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_square_root_fail_negative(self):
        url = f"{BASE_URL}/calc/square_root/-64"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_square_root_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/square_root/-five"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_square_root_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/square_root/six"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    # ***********************************
    # *** LOG BASE 10 UNIT TEST CASES
    # ***********************************

    def test_api_log_base_10_positive(self):
        url = f"{BASE_URL}/calc/log_base_10/1000"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_log_base_10_positive(self):
        url = f"{BASE_URL}/calc/log_base_10/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_log_base_10_decimal(self):
        url = f"{BASE_URL}/calc/log_base_10/25.4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_log_base_10_decimal(self):
        url = f"{BASE_URL}/calc/log_base_10/0.01"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_log_base_10_fail_negative(self):
        url = f"{BASE_URL}/calc/log_base_10/-5"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_log_base_10_fail_negative(self):
        url = f"{BASE_URL}/calc/log_base_10/-2.56"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_log_base_10_fail_zero(self):
        url = f"{BASE_URL}/calc/log_base_10/0.0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_log_base_10_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/log_base_10/nine"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )

    def test_api_log_base_10_fail_datatypeincorrect(self):
        url = f"{BASE_URL}/calc/log_base_10/n***%^6e"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            cm.exception.code, http.client.BAD_REQUEST, f"Unexpected error code from {url}"
        )
