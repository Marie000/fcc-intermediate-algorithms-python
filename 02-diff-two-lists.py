import unittest
 
'''
 Diff Two Lists

Compare two lists and return a new list with any items only found in one of the two 
given lists, but not both. In other words, return the symmetric difference of the 
two lists.

Note: You can return the list with its elements in any order.

 '''

def diff_lists(lst1, lst2):
    new_lst = []
    return new_lst

print(diff_lists([1, 2, 3, 5], [1, 2, 3, 4, 5]))
 
"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertIsInstance(diff_lists([1, 2, 3, 5], [1, 2, 3, 4, 5]), list)

    def test2(self):
        self.assertCountEqual(diff_lists(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]), ["pink wool"])
    
    def test3(self):
        self.assertEqual(len(diff_lists(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])), 1)
    
    def test4(self):
        self.assertCountEqual(diff_lists(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]), ["diorite", "pink wool"])
    
    def test5(self):
        self.assertEqual(len(diff_lists(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])), 2)
    
    def test6(self):
        self.assertCountEqual(diff_lists(["andesite", "grass", "dirt", "dead shrub"], ["andesite", "grass", "dirt", "dead shrub"]), [])
    
    def test7(self):
        self.assertEqual(len(diff_lists(["andesite", "grass", "dirt", "dead shrub"], ["andesite", "grass", "dirt", "dead shrub"])), 0)
    
    def test8(self):
        self.assertCountEqual(diff_lists([1, 2, 3, 5], [1, 2, 3, 4, 5]), [4])
    
    def test9(self):
        self.assertCountEqual(diff_lists([1, "calf", 3, "piglet"], [1, "calf", 3, 4]), ["piglet", 4])

    def test10(self):
        self.assertCountEqual(diff_lists([], ["snuffleupagus", "cookie monster", "elmo"]), ["snuffleupagus", "cookie monster", "elmo"])

    def test11(self):
        self.assertCountEqual(diff_lists([1, "calf", 3, "piglet"], [7, "filly"]), [1, "calf", 3, "piglet", 7, "filly"])


if __name__ == "__main__":
    unittest.main()
