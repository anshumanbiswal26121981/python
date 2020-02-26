#  Binary search to return the index of the searched number in a sorted array
#  author: anshuman biswal


class BinarySearch:

    def search_index_number(self, number, array, start, end):
        if len(array) == 0:
            raise ValueError("You canot search for a number in an empty array")
        if start == end:
            if array[start] == number:
                return start
            else:
                raise IndexError("Element not found")

        mid = int((start + end) / 2)
        if array[mid] == number:
            return mid
        elif array[mid] > number:
            return self.search_index_number(number, array,start, mid - 1)
        else:
            return self.search_index_number(number, array, mid + 1, end)
