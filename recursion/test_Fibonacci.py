from unittest import TestCase

from python.recursion.Fibonacci import Fibonacci


class TestFibonacci(TestCase):
    fibonacciInstance = Fibonacci()

    def test_fibonacci_for_zerothterm(self):
        self.assertRaises(ValueError, self.fibonacciInstance.fibonacci, 0)

    def test_fibonacci_for_1term(self):
        self.assertEqual(self.fibonacciInstance.fibonacci(1), 0)

    def test_fibonacci_for_2term(self):
        self.assertEqual(self.fibonacciInstance.fibonacci(2), 1)

    def test_fibonacci_for_3term(self):
        self.assertEqual(self.fibonacciInstance.fibonacci(3), 1)

    def test_fibonacci_for_4term(self):
        self.assertEqual(self.fibonacciInstance.fibonacci(4), 2)

    def test_fibonacci_for_5term(self):
        self.assertEqual(self.fibonacciInstance.fibonacci(5), 3)