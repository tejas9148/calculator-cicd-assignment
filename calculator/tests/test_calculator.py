
import unittest

from calculator.app import add, subtract, multiply


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_negative_subtraction_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_zero_is_rejected(self):
        with self.assertRaises(ValueError):
            add(0, 5)

    def test_negative_input_is_rejected(self):
        with self.assertRaises(ValueError):
            multiply(-2, 5)

    def test_non_integer_input_is_rejected(self):
        with self.assertRaises(TypeError):
            add(2.5, 5)


if __name__ == "__main__":
    unittest.main()
