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

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(1, self.calc.substract(3, 2))
        self.assertEqual(-2, self.calc.substract(2, 4))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_raiz_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.raiz(16))
        self.assertEqual(5, self.calc.raiz(25))
    
    def test_raiz_method_fails_with_negative_parameter(self):
        self.assertRaises(ValueError, self.calc.raiz, -4)
        self.assertRaises(ValueError, self.calc.raiz, -25)
    
    def test_raiz_root_method_fails_with_non_numeric_parameter(self):
        self.assertRaises(ValueError, self.calc.raiz, "4")
        self.assertRaises(ValueError, self.calc.raiz, None)
        self.assertRaises(ValueError, self.calc.raiz, object())
    
    def test_log_base10_method_returns_correct_result(self):
        self.assertAlmostEqual(1, self.calc.log_base10(10))
        self.assertAlmostEqual(2, self.calc.log_base10(100))
    
    def test_log_base10_fails_with_non_positive_parameter(self):
        self.assertRaises(ValueError, self.calc.log_base10, -1)
        self.assertRaises(ValueError, self.calc.log_base10, -100)
    
    def test_multiply_method_returns_correct_result(self):
        self.assertAlmostEqual(6, self.calc.multiply(2, 3))
        self.assertAlmostEqual(2, self.calc.multiply(2, 1))
    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(1, self.calc.power(3, 0))
        self.assertEqual(27, self.calc.power(3, 3))
    
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
        
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
    
    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "4", 4)
        self.assertRaises(TypeError, self.calc.divide, 4, "4")
        self.assertRaises(TypeError, self.calc.divide, "4", "4")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 4, 0)
        self.assertRaises(TypeError, self.calc.divide, 4, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
