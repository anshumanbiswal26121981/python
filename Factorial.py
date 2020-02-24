#  factorial(3) = 3*2*1=6
#  author: anshuman biswal


class Factorial:
    def factorial(self, num):
        if num < 0:
            raise ValueError("Factorial of negative numbers cannot be calculated")
        elif num == 0 or num == 1:
            return 1
        else:
            return num * self.factorial(num - 1)
