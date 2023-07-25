import unittest

"""
Pig Latin

Pig Latin is a way of altering English Words. The rules are as follows:

- If a word begins with a consonant, take the first consonant or 
consonant cluster, move it to the end of the word, and add ay to it.

- If a word begins with a vowel, just add way at the end.

Translate the provided string to Pig Latin. Input strings are guaranteed 
to be English words in all lowercase.

"""

def translate_pig_latin(string):
    return string

print(translate_pig_latin("consonant"))


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(translate_pig_latin('california'), 'aliforniacay')

    def test2(self):
        self.assertEqual(translate_pig_latin('paragraphs'), 'aragraphspay')

    def test3(self):
        self.assertEqual(translate_pig_latin('glove'), 'oveglay')

    def test4(self):
        self.assertEqual(translate_pig_latin('algorithm'), 'algorithmway')

    def test5(self):
        self.assertEqual(translate_pig_latin('eight'), 'eightway')

    def test6(self):
        self.assertEqual(translate_pig_latin('schwartz'), 'artzschway')

    def test7(self):
        self.assertEqual(translate_pig_latin('rhythm'), 'rhythmay')
        
if __name__ == "__main__":
    unittest.main()



