import unittest

"""
Steamroller

Flatten a nested list. You must account for varying levels of nesting.


"""

# note to self: this is not an ideal solution. Still don't know where 
# the None came from in the first place. 

def steamroll_list(lst):
    result = []
    def flatten(lst):
        if type(lst) != list:
            return lst
        else:
            for item in lst:
                result.append(flatten(item))
    for item in lst:
        result.append(flatten(item))

    return [x for x in result if x is not None]

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
