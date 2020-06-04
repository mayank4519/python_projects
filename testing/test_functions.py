from unittest import TestCase
from functions import divide,multiply

class Test(TestCase):
    def test_divide(self):
        dividend = 15
        divisor = 5
        expected = 3.0
        self.assertAlmostEqual(divide(dividend, divisor), expected, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected = 0
        self.assertEqual(divide(dividend, divisor), expected)

    def test_divide_b_zero(self):
        with self.assertRaises(ValueError):
            divide(25,0)

    def test_multiply(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)

    def test_multiply_by_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_result(self):
        input = (3, 5)
        expected = 15
        self.assertEqual(multiply(*input), expected)

    def test_multiply_result_with_zero(self):
        input = (3, 5, 0)
        expected = 15
        self.assertEqual(multiply(*input), expected)

    def test_multiply_negative(self):
        input = (3,-5)
        expected = -15
        self.assertEqual(multiply(*input), expected)

    def test_multiply_float(self):
        input = (3,5.0)
        expected = 15.0
        self.assertEqual(multiply(*input), expected)
