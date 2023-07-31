import unittest

"""
Seek and Destroy

You will be provided with an initial list (the first argument in the destroyer 
function), followed by one or more arguments. Remove all elements from the 
initial list that are of the same value as these arguments.

"""

def destroyer(lst, *args):
    return [x for x in lst if x not in args]

print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))

"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertListEqual(destroyer([1, 2, 3, 1, 2, 3], 2, 3), [1, 1])

    def test2(self):
        self.assertListEqual(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3), [1, 5, 1])

    def test3(self):
        self.assertListEqual(destroyer([3, 5, 1, 2, 2], 2, 3, 5), [1])

    def test4(self):
        self.assertListEqual(destroyer([2, 3, 2, 3], 2, 3), [])

    def test5(self):
        self.assertListEqual(destroyer(["tree", "hamburger", 53], "tree", 53), ["hamburger"])

    def test6(self):
        self.assertListEqual(destroyer(["possum", "trollo", 12, "safari", "hotdog", 92, 65, "grandma", "bugati", "trojan", "yacht"], "yacht", "possum", "trollo", "safari", "hotdog", "grandma", "bugati", "trojan"), [12, 92, 65])

    

if __name__ == "__main__":
    unittest.main()
