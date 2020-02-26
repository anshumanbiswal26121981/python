#  Biggest number in an array using recursion
#  author: anshuman biswal


class BiggestNumberRecursive:
    def find_biggest_number(self, array, length):
        length_of_array_passed = len(array)
        if length_of_array_passed != length:
            raise ValueError("the length of array passsed and length doesnot match")
        if length_of_array_passed == 0:
            raise ValueError("we cannot find biggest number in an empty array")
        if length == 1:
            return array[0]
        else:
            return max(self.find_biggest_number(array[:length-1], length-1), array[length-1])
