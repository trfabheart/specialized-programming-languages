import unittest
from unittest.mock import patch
from classes import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Test checks correct input of numbers and operator
    @patch('builtins.input', side_effect=['10', '+', '1'])
    def test_get_input_valid(self, mock_input):
        num1, operator, num2 = self.calc.get_input()
        self.assertEqual(num1, 10.0)
        self.assertEqual(operator, '+')
        self.assertEqual(num2, 1.0)

    # Test checks the use of memory and square root operator
    @patch('builtins.input', side_effect=['m', '√'])
    def test_get_input_memory_sqrt(self, mock_input):
        self.calc.memory.set_memory(16.0)
        num1, operator, num2 = self.calc.get_input()
        self.assertEqual(num1, 16.0)
        self.assertEqual(operator, '√')
        self.assertIsNone(num2)

    # Test checks handling invalid operator and prompt for valid operator
    @patch('builtins.input', side_effect=['$', '+'])
    def test_get_operator_invalid_then_valid(self, mock_input):
        operator = self.calc.get_operator()
        self.assertEqual(operator, '+')

    # Test checks recognition of valid operators
    def test_check_operator_valid(self):
        self.assertTrue(self.calc.check_operator('+'))
        self.assertTrue(self.calc.check_operator('-'))
        self.assertTrue(self.calc.check_operator('*'))
        self.assertTrue(self.calc.check_operator('/'))
        self.assertTrue(self.calc.check_operator('^'))
        self.assertTrue(self.calc.check_operator('√'))
        self.assertTrue(self.calc.check_operator('%'))

    # Test checks recognition of invalid operators
    def test_check_operator_invalid(self):
        self.assertFalse(self.calc.check_operator('&'))
        self.assertFalse(self.calc.check_operator('!'))
        self.assertFalse(self.calc.check_operator('incorrect'))
        self.assertFalse(self.calc.check_operator('1'))

    # Test checks setting and getting memory value
    def test_memory_set_get(self):
        self.calc.memory.set_memory(10)
        self.assertEqual(self.calc.memory.get_memory(), 10)

    # Test checks clearing memory
    def test_memory_clear(self):
        self.calc.memory.set_memory(10)
        self.calc.memory.clear_memory()
        self.assertEqual(self.calc.memory.get_memory(), 0)

    # Test checks adding to history and checking for a record
    def test_history_add_and_show(self):
        self.calc.history.add_to_history("2 + 2", 4)
        self.assertIn("2 + 2 = 4", self.calc.history._History__history)

    # Test checks setting the number of decimal places
    def test_set_decimal_places(self):
        with patch('builtins.input', side_effect=['2']):
            self.calc.decimal_point.set_decimal_point()
            self.assertEqual(self.calc.decimal_point.get_decimal_point(), 2)

    # Test checks handling invalid input for decimal places
    def test_set_decimal_places_invalid(self):
        with patch('builtins.input', side_effect=['-1']):
            with self.assertRaises(ValueError):
                self.calc.decimal_point.set_decimal_point()

    # Tests for basic operations: addition, subtraction, multiplication, division
    def test_addition(self):
        self.assertEqual(self.calc.calculate(2, '+', 2), 4)
        self.assertEqual(self.calc.calculate(-2, '+', -2), -4)
        self.assertEqual(self.calc.calculate(-2, '+', 2), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.calculate(2, '-', 2), 0)
        self.assertEqual(self.calc.calculate(-2, '-', -2), 0)
        self.assertEqual(self.calc.calculate(2, '-', 4), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.calculate(2, '*', 2), 4)
        self.assertEqual(self.calc.calculate(2, '*', 0), 0)
        self.assertEqual(self.calc.calculate(-2, '*', 2), -4)

    def test_division(self):
        self.assertEqual(self.calc.calculate(4, '/', 2), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate(2, '/', 0)

    # Test for square root operation
    def test_square_root(self):
        self.assertEqual(self.calc.calculate(4, '√', None), 2)
        with self.assertRaises(ValueError):
            self.calc.calculate(-4, '√', None)

    # Test for modulo operation
    def test_modulo(self):
        self.assertEqual(self.calc.calculate(5, '%', 3), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate(1, '%', 0)

    # Tests for exponentiation operation
    def test_exponentiation(self):
        self.assertEqual(self.calc.calculate(2, '^', 2), 4)
        self.assertEqual(self.calc.calculate(2, '^', 0), 1)
        self.assertEqual(self.calc.calculate(-2, '^', 2), 4)
        self.assertEqual(self.calc.calculate(2, '^', -1), 0.5)

if __name__ == '__main__':
    unittest.main()