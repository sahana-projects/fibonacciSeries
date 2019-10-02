from django.db import models

# Create your models here.

class FibonacciCalculator():
    """docstring for FibonacciCalculator."""

    def __init__(self, arg):
        super(FibonacciCalculator, self).__init__()
        self.arg = arg

    def get_fibonacci_seq(number):
        seq = [0, 1]

        for i in range(2,number+1):
            tmp = seq[i-1] + seq[i-2]
            seq.append(tmp)
        return seq[-5:]
