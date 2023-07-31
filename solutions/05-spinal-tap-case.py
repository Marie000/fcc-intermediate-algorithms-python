import unittest

"""
Spinal Tap Case

Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.

hint: if you want to replace part of the string using regex, you might want to 
import re

"""

import re

def spinal_case(string):
    #replace _ with -
    string = string.replace('_', '-')
    #add spaces before uppercase letters
    string = re.sub(r'(\B)([A-Z])', r"\1 \2", string)
    #replace spaces with dashes
    string = string.replace(' ', '-').lower()

    return string

print(spinal_case('This Is Spinal Tap'))



"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(spinal_case("This Is Spinal Tap"), "this-is-spinal-tap")

    def test2(self):
        self.assertEqual(spinal_case("thisIsSpinalTap"), "this-is-spinal-tap")
        
    def test3(self):
        self.assertEqual(spinal_case("The_Andy_Griffith_Show"), "the-andy-griffith-show")
        
    def test4(self):
        self.assertEqual(spinal_case("Teletubbies say Eh-oh"), "teletubbies-say-eh-oh")
        
    def test5(self):
        self.assertEqual(spinal_case("AllThe-small Things"), "all-the-small-things")
        
if __name__ == "__main__":
    unittest.main()

