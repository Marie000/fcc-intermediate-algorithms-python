import unittest

"""
DNA Pairing

Pairs of DNA strands consist of nucleobase pairs. Base pairs are represented 
by the characters AT and CG, which form building blocks of the DNA double helix.

The DNA strand is missing the pairing element. Write a function to match the missing 
base pairs for the provided DNA strand. For each character in the provided string, 
find the base pair character. Return the results as a 2d array.

For example, for the input GCG, return [["G", "C"], ["C","G"], ["G", "C"]]

The character and its pair are paired up in a list, and all the lists are grouped 
into one encapsulating list.

"""

DNA_PAIRS = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

def pair_elements(string):
    return [[letter, DNA_PAIRS[letter]] for letter in string]

print(pair_elements("GCG"))


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertListEqual(pair_elements("ATCGA"), [["A","T"],["T","A"],["C","G"],["G","C"],["A","T"]])

    def test2(self):
        self.assertListEqual(pair_elements("TTGAG"), [["T","A"],["T","A"],["G","C"],["A","T"],["G","C"]])

    def test3(self):
        self.assertListEqual(pair_elements("CTCTA"), [["C","G"],["T","A"],["C","G"],["T","A"],["A","T"]])

if __name__ == "__main__":
    unittest.main()

