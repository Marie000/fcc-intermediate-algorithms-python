import unittest

"""
Drop it

Given the list lst, iterate through and remove each element starting from the first 
element (the 0 index) until the function func returns true when the iterated element 
is passed through it.

Then return the rest of the list once the condition is satisfied, otherwise, lst 
should be returned as an empty lst.

"""
def drop_elements(lst, func):
    result = []
    for i, item in enumerate(lst):
        if func(item):
            result = lst[i:]
            break

    return result

print(drop_elements([1, 2, 3], lambda n: n<3))



"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertListEqual(drop_elements([1, 2, 3, 4], lambda n: n>= 3), [3, 4])

    def test2(self):
        self.assertListEqual(drop_elements([0, 1, 0, 1], lambda n: n == 1), [1, 0, 1])

    def test3(self):
        self.assertListEqual(drop_elements([1, 2, 3], lambda n: n > 0), [1, 2, 3])

    def test4(self):
        self.assertListEqual(drop_elements([1, 2, 3, 4], lambda n: n>5), [])

    def test5(self):
        self.assertListEqual(drop_elements([1, 2, 3, 7, 4], lambda n: n> 3), [7, 4])

    def test6(self):
        self.assertListEqual(drop_elements([1, 2, 3, 9, 2], lambda n: n> 2), [3, 9, 2])

if __name__ == "__main__":
    unittest.main()




