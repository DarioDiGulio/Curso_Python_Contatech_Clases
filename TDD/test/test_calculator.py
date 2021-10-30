import unittest
from unittest import TestCase
from parameterized import parameterized
from TDD.src.Calculator import Calculator


class CalculatorTest(TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    @parameterized.expand([
        ["11", "2", "4"],
        ["11", "11", "4"],
        ["78", "11", "17"],
    ])
    def test_add(self, num1, num2, expected):
        # When
        result = self.calculator.add(num1, num2)

        # Then
        self.assert_result(result, int(expected))

    @parameterized.expand([
        ["11", "2", "4"],
        ["11", "11", "4"],
        ["78", "11", "17"],
    ])
    def test_substraction(self, num1, num2, expected):
        # When
        result = self.calculator.substraction(44, 22)

        # Then
        self.assert_result(result, 4)

    def test_multiplication(self):
        # When
        result = self.calculator.multiplication(22, 31)

        # Then
        self.assert_result(result, 12)

    def assert_result(self, result, expected):
        self.assertEqual(result, expected, f'Debería ser {expected} y fue {result}')


if __name__ == '__main__':
    unittest.main()
