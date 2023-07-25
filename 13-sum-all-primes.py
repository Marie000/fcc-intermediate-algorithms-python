import unittest

"""
Sum All Primes

A prime number is a whole number greater than 1 with exactly two divisors: 1 and 
itself. For example, 2 is a prime number because it is only divisible by 1 and 2. 
In contrast, 4 is not prime since it is divisible by 1, 2 and 4.

Rewrite sum_primes so it returns the sum of all prime numbers that are less than or 
equal to num.

"""

def sum_primes(n):
    return n

print(sum_primes(10))

"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertIsInstance(sum_primes(10), int)

    def test2(self):
        self.assertEqual(sum_primes(10), 17)

    def test3(self):
        self.assertEqual(sum_primes(977), 73156)


if __name__ == "__main__":
    unittest.main()