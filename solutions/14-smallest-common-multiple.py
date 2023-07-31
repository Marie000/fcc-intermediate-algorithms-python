import unittest

"""
Smallest Common Multiple

Find the smallest common multiple of the provided parameters that can be evenly 
divided by both, as well as by all sequential numbers in the range between these 
parameters.

The range will be a list of two numbers that will not necessarily be in numerical 
order.

For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that 
is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.

"""
import math

def is_multiplier(multiplier, n):
    return multiplier % n == 0

def is_multiplier_for_range(multiplier, range_):
    result = True
    for n in range_:
        if not is_multiplier(multiplier, n):
            result = False
            break
    return result

def smallest_commons(lst):
    first, last = sorted(lst)
    original_range = range(first,last+1)
    max_possible = math.prod(original_range)
    answer = max_possible
    for n in range(last, max_possible):
        if is_multiplier_for_range(n, original_range):
            answer = n
            break
    return answer


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertIsInstance(smallest_commons([1,5]), int)

    def test2(self):
        self.assertEqual(smallest_commons([1,5]), 60)

    def test3(self):
        self.assertEqual(smallest_commons([5,1]), 60)

    def test4(self):
        self.assertEqual(smallest_commons([2,10]), 2520)

    def test5(self):
        self.assertEqual(smallest_commons([1,13]), 360360)

    def test6(self):
        self.assertEqual(smallest_commons([23,18]), 6056820)


if __name__ == "__main__":
    unittest.main()
