import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # ***********************************
    # *** ADD UNIT TEST CASES ***
    # ***********************************

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    # ***********************************
    # *** SUBSTRACT UNIT TEST CASES ***
    # ***********************************

    # ***********************************
    # *** MULTIPLY UNIT TEST CASES ***
    # ***********************************

    # ***********************************
    # *** DIVIDE UNIT TEST CASES ***
    # ***********************************

    # case 1:
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    # case 2:
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    # case 3:
    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    # ***********************************
    # *** POWER UNIT TEST CASES ***
    # ***********************************

    # ***********************************
    # *** SQUARE ROOT UNIT TEST CASES ***
    # ***********************************
    
    # case 1: return correct result
    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(3, self.calc.square_root(9))
        self.assertEqual(4, self.calc.square_root(16))
        self.assertEqual(5, self.calc.square_root(25))
        self.assertEqual(6, self.calc.square_root(36))
        self.assertEqual(7, self.calc.square_root(49))
        self.assertEqual(8, self.calc.square_root(64))

    # case 2: return fails for negative numbers
    def test_square_root_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.square_root, -25)
        self.assertRaises(TypeError, self.calc.square_root, -36)

    # case 3: return fails for data type incorrect
    def test_square_root_method_fails_data_type_incorrect(self):
        self.assertRaises(TypeError, self.calc.square_root("five"))
        self.assertRaises(TypeError, self.calc.square_root("*****"))
        self.assertRaises(TypeError, self.calc.square_root("text"))
        self.assertRaises(TypeError, self.calc.square_root("this is a exception"))

    # case 4: return correct results for decimals numbers
    def test_square_root_method_return_correct_result_decimal_number(self):
        self.assertEqual(1.5, self.calc.square_root(2.25))

    # case 5: return correct result for square root for zero
    def test_square_root_method_return_correct_result_zero(self):
        self.assertEqual(0, self.calc.square_root(0))
    
    # case 6: return correct result for big numbers
    def test_square_root_method_return_correct_result_big_number(self):
        self.assertEqual(31622.7766, self.calc.square_root(999999999))

    # case 5: return correct result

    # ***********************************
    # *** LOG BASE 10 UNIT TEST CASES
    # ***********************************
    
    # case 1: return correct result
    def test_logbase10_method_return_correct_result(self):
        self.assertEqual(2.0, self.calc.log_base_10(100)) 
        self.assertEqual(3.0, self.calc.log_base_10(1000))
        self.assertEqual(0.0, self.calc.log_base_10(1))

    # case 2: return correct result for decimal number
    def test_logbase10_method_return_correct_result_decimal_numbers(self):
        self.assertAlmostEqual(1.4048, self.calc.log_base_10(25.4))

    # case 3: return correct result for decimal number minor than 1
    def test_logbase10_method_return_correct_result_decimal_number_minor_than1(self):
        self.assertEqual(-2.0, self.calc.log_base_10(0.01))

    # case 4: return correct result for 
    def test_logbase10_method_fails_with_zero_or_negative_number(self):
        self.assertRaises(TypeError, self.calc.log_base_10(-5))
        self.assertRaises(TypeError, self.calc.log_base_10(-2.56))
        self.assertRaises(TypeError, self.calc.log_base_10(0.0))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
