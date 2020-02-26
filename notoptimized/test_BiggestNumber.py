from unittest import TestCase

from python.notoptimized.BiggestNumber import BiggestNumber


class TestBiggestNumber(TestCase):
    biggest_number_instance = BiggestNumber()

    def test_find_biggest_number_with10_inputs(self):
        arr = [1, 2, 3, 4, 8, 10, 0, 8, 9, 5]
        self.assertEqual(10, self.biggest_number_instance.findBiggestNumber(arr))

    def test_find_biggest_number_with5_inputs(self):
        arr = [500, 900,1000, 100, 0]
        self.assertEqual(1000, self.biggest_number_instance.findBiggestNumber(arr))

    def test_find_biggest_number_with0_inputs(self):
        arr = []
        self.assertRaises(ValueError, self.biggest_number_instance.findBiggestNumber, arr)

