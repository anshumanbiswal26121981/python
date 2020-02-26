from unittest import TestCase

from python.recursion.BinarySearch import BinarySearch


class TestBinarySearch(TestCase):
    binary_search_instance = BinarySearch()

    def test_search_index_number_right_of_mid(self):
        array = [10, 20, 30, 40, 50, 60, 70]
        self.assertEqual(5, self.binary_search_instance.search_index_number(60, array, 0, len(array) - 1))

    def test_search_index_number_left_of_mid(self):
        array = [10, 20, 30, 40, 50, 60, 70]
        self.assertEqual(1, self.binary_search_instance.search_index_number(20, array, 0, len(array) - 1))

    def test_search_index_number_at_mid(self):
        array = [10, 20, 30, 40, 50, 60, 70]
        self.assertEqual(3, self.binary_search_instance.search_index_number(40, array, 0, len(array) - 1))

    def test_search_index_number_not_found(self):
        array = [10, 20, 30, 40, 50, 60, 70]
        self.assertRaises(IndexError, self.binary_search_instance.search_index_number, 90, array, 0, len(array) - 1)

    def test_search_index_number_in_empty_array(self):
        array = []
        self.assertRaises(ValueError, self.binary_search_instance.search_index_number, 40, array, 0, len(array) - 1)


