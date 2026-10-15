# calculator/tests.py

import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_addition(self) -> None:
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self) -> None:
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self) -> None:
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self) -> None:
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self) -> None:
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self) -> None:
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_empty_expression(self) -> None:
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")

    # New factorial tests
    def test_factorial_zero(self) -> None:
        result = self.calculator.evaluate("0!")
        self.assertEqual(result, 1)

    def test_factorial_one(self) -> None:
        result = self.calculator.evaluate("1!")
        self.assertEqual(result, 1)

    def test_factorial_five(self) -> None:
        result = self.calculator.evaluate("5!")
        self.assertEqual(result, 120)

    def test_factorial_with_other_operations(self) -> None:
        result = self.calculator.evaluate("3! + 4")
        self.assertEqual(result, 10)  # 3! = 6, 6 + 4 = 10

    def test_factorial_multiplication(self) -> None:
        result = self.calculator.evaluate("3 * 4!")
        self.assertEqual(result, 72)  # 4! = 24, 3 * 24 = 72

    def test_factorial_negative(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("-5!")

    def test_factorial_invalid_token(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("abc!")


if __name__ == "__main__":
    unittest.main()