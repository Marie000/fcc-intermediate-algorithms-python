import unittest

"""
Steamroller

Flatten a nested list. You must account for varying levels of nesting.


"""

def steamroll_list(lst):
    return lst

print(steamroll_list([1, [2], [3, [[4]]]]))

"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertListEqual(steamroll_list([[["a"]], [["b"]]]), ["a", "b"])

    def test2(self):
        self.assertListEqual(steamroll_list([1, [2], [3, [[4]]]]), [1, 2, 3, 4])

    def test3(self):
        self.assertListEqual(steamroll_list([1, [], [3, [[4]]]]), [1, 3, 4])

    def test4(self):
        self.assertListEqual(steamroll_list([1, {}, [3, [[4]]]]), [1, {}, 3, 4])


if __name__ == "__main__":
    unittest.main()
