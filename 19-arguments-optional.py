import unittest

"""
Arguments Optional

Create a function that sums two arguments together. If only one argument is 
provided, then return a function that expects one argument and returns the sum.

For example, addTogether(2, 3) should return 5, and addTogether(2) should 
return a function.

Calling this returned function with a single argument will then return the 
sum:

sum_two_and = add_together(2);

sum_two_and(3) returns 5.

If either argument isn't a valid number, return None.

"""

def add_together(*args):
    return False

print(add_together(2,3))


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(add_together(2,3),5)

    def test2(self):
        self.assertEqual(add_together(23,30),53)

    def test3(self):
        self.assertEqual(add_together("2",3),None)

    def test4(self):
        self.assertEqual(add_together(5, None), None)

    def test5(self):
        self.assertEqual(add_together("string"), None)

    def test6(self):
        self.assertEqual(callable(add_together(5)), True)

    def test7(self):
        self.assertEqual(add_together(5)(7), 12)

    def test8(self):
        self.assertEqual(add_together(2)([3]), None)

if __name__ == "__main__":
    unittest.main()


