#
#  Fibonacci series: 0,1,1,2,3,5,8,13,21,...
#  fibonacci(5) => fifth term in the fibonacci series = 3
#  author: anshuman biswal


class Fibonacci:
    def fibonacci(self, nth_term):
        if nth_term < 1:
            raise ValueError("Fibonacci of atleast 1th term is needed. The term cannot be less than 1")
        elif nth_term == 1 or nth_term == 2:
            return nth_term - 1
        else:
            return self.fibonacci(nth_term-2) + self.fibonacci(nth_term-1)


