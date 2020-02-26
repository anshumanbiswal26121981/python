from unittest import TestCase

from python.notoptimized.BiggestNumberRecursive import BiggestNumberRecursive


class TestBiggestNumberrecursive(TestCase):
    biggest_number_recursive_instance = BiggestNumberRecursive()

    def test_find_biggest_number_with10_inputs(self):
        arr = [1, 2, 3, 4, 8, 10, 0, 8, 9, 5]
        self.assertEqual(10, self.biggest_number_recursive_instance.find_biggest_number(arr, len(arr)))

    def test_find_biggest_number_with5_inputs(self):
        arr = [500, 900,1000, 100, 0]
        self.assertEqual(1000, self.biggest_number_recursive_instance.find_biggest_number(arr, len(arr)))

    def test_find_biggest_number_with0_inputs(self):
        arr = []
        self.assertRaises(ValueError, self.biggest_number_recursive_instance.find_biggest_number, arr, len(arr))

