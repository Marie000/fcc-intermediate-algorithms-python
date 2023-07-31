import unittest

'''
Sum All Numbers in a Range

We'll pass you a list of two numbers. Return the sum of those two numbers plus the 
sum of all the numbers between them. The lowest number will not always come first.

For example, sum_all([4,1]) should return 10 because sum of all the numbers between
1 and 4 (both inclusive) is 10.

'''

def sum_all(lst):
    sorted_lst = sorted(lst)
    start = sorted_lst[0]
    end = sorted_lst[1] + 1
    return sum(range(start, end))

print(sum_all([1, 4]))


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertIsInstance(sum_all([1,4]), int)

    def test2(self):
        self.assertEqual(sum_all([1,4]), 10)
    
    def test3(self):
        self.assertEqual(sum_all([4,1]), 10)

    def test4(self):
        self.assertEqual(sum_all([5,10]), 45)

    def test5(self):
        self.assertEqual(sum_all([10,5]), 45)


if __name__ == "__main__":
    unittest.main()
