import unittest

"""
Search and Replace

Perform a search and replace on the sentence using the arguments provided 
and return the new sentence.

First argument is the sentence to perform the search and replace on.

Second argument is the word that you will be replacing (before).

Third argument is what you will be replacing the second argument with 
(after).

Note: Preserve the case of the first character in the original word when 
you are replacing it. For example if you mean to replace the word Book 
with the word dog, it should be replaced as Dog

"""

def my_replace(string, before, after):
    return string

print(my_replace("A quick brown fox jumped over the lazy dog", "jumped", "leaped"))



"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(my_replace("Let us go to the store", "store", "mall"), "Let us go to the mall")

    def test2(self):
        self.assertEqual(my_replace("He is Sleeping on the couch", "Sleeping", "sitting"), "He is Sitting on the couch")

    def test3(self):
        self.assertEqual(my_replace("I think she should look up there", "up", "Down"), "I think she should look down there")

    def test4(self):
        self.assertEqual(my_replace("This has a spellngi error", "spellngi", "spelling"), "This has a spelling error")

    def test5(self):
        self.assertEqual(my_replace("His name is Tom", "Tom", "john"), "His name is John")

    def test6(self):
        self.assertEqual(my_replace("Let us get back to more Coding", "Coding", "algorithms"),"Let us get back to more Algorithms")


if __name__ == "__main__":
    unittest.main()

