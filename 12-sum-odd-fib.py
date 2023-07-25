import unittest

"""
Sum All Odd Fibonacci Numbers

Given a positive integer num, return the sum of all odd Fibonacci numbers 
that are less than or equal to num.

The first two numbers in the Fibonacci sequence are 0 and 1. Every additional 
number in the sequence is the sum of the two previous numbers. The first seven 
numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5 and 8.

For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less 
than or equal to 10 are 1, 1, 3, and 5.

"""

def sum_fibs(num):
    return num

print(sum_fibs(4))


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertIsInstance(sum_fibs(1), int)

    def test2(self):
        self.assertEqual(sum_fibs(1000), 1785)

    def test3(self):
        self.assertEqual(sum_fibs(4000000), 4613732)

    def test4(self):
        self.assertEqual(sum_fibs(4), 5)

    def test5(self):
        self.assertEqual(sum_fibs(75024), 60696)

    def test6(self):
        self.assertEqual(sum_fibs(75025), 135721)

if __name__ == "__main__":
    unittest.main()