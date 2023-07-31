import unittest

"""
Missing letters

Find the missing letter in the passed letter range and return it.

If all letters are present in the range, return None.

"""

def fear_no_letter(string):
    missing_letter = None
    for i, letter in enumerate(string):
        if (i > 0):
            actual_previous_letter = string[i - 1]
            expected_previous_letter = chr(ord(letter) - 1)
            if ord(actual_previous_letter) + 1 != ord(letter):
                missing_letter = expected_previous_letter
            
    return missing_letter

print(fear_no_letter("abcd"))



"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(fear_no_letter("abce"), "d")

    def test2(self):
        self.assertEqual(fear_no_letter("abcdefghjklmno"), "i")

    def test3(self):
        self.assertEqual(fear_no_letter("stvwx"), "u")

    def test4(self):
        self.assertEqual(fear_no_letter("bcdf"), "e")

    def test5(self):
        self.assertEqual(fear_no_letter("abcdefghijklmnopqrstuvwxyz"), None)

if __name__ == "__main__":
    unittest.main()

