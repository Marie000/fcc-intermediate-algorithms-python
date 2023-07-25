import unittest

"""
Sorted Union

Write a function that takes two or more lists and returns a new list of unique 
values in the order of the original provided lists.

In other words, all values present from all lists should be included in their 
original order, but with no duplicates in the final lists.

The unique numbers should be sorted by their original order, but the final list
should not be sorted in numerical order.

Check the assertion tests for examples.


"""

def unite_unique(*lists):
    return lists


print(unite_unique([1, 2, 3], [5, 2, 1, 4], [2, 1]))

"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):


    def test1(self):
        self.assertListEqual(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]), [1, 3, 2, 5, 4])

    def test2(self):
        self.assertListEqual(unite_unique([1, 2, 3], [5, 2, 1]), [1, 2, 3, 5])

    def test3(self):
        self.assertListEqual(unite_unique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]), [1, 2, 3, 5, 4, 6, 7, 8])

    def test4(self):
        self.assertListEqual(unite_unique([1, 3, 2], [5, 4], [5, 6]), [1, 3, 2, 5, 4, 6])

    def test5(self):
        self.assertListEqual(unite_unique([1, 3, 2, 3], [5, 2, 1, 4], [2, 1]), [1, 3, 2, 5, 4])

if __name__ == "__main__":
    unittest.main()
