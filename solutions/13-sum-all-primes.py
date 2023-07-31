import unittest

"""
Sum All Primes

A prime number is a whole number greater than 1 with exactly two divisors: 1 and 
itself. For example, 2 is a prime number because it is only divisible by 1 and 2. 
In contrast, 4 is not prime since it is divisible by 1, 2 and 4.

Rewrite sum_primes so it returns the sum of all prime numbers that are less than or 
equal to num.

"""

def is_prime(n):
    prime = True
    for num in range(2,n-1):
        if n%num == 0:
            prime = False
            break
    return prime
        

def sum_primes(n):
    total = 0
    for num in range(2, n+1):
        if (is_prime(num)):
            total += num
    return total
    

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