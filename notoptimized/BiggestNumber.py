#  Biggest number in an array
#  author: anshuman biswal


class BiggestNumber:
    def findBiggestNumber(self, arr):
        length_of_array = len(arr)
        if length_of_array <= 0:
            raise ValueError("We cannot find largest number in an empty array")

        biggest_number = arr[0]

        for i in range(1, length_of_array):
            if arr[i] > biggest_number:
                biggest_number = arr[i]

        return biggest_number
