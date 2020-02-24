from unittest import TestCase

from python.recursion.Factorial import Factorial


class TestFactorial(TestCase):
    factorialInstance = Factorial()

    def test_factorial(self):
        self.assertEqual(self.factorialInstance.factorial(3), 6)

    def test_factorial_negative(self):
        self.assertRaises(ValueError, self.factorialInstance.factorial, -1)
