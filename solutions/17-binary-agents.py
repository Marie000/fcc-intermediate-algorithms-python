import unittest

"""
Binary Agents

Return an English translated sentence of the passed binary string.

The binary string will be space separated.

"""

def binary_agent(string):
    letter_list = string.split(' ')
    result = ''
    for letter in letter_list:
        result += chr(int(letter,2))
    return result

print(binary_agent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"))



"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(binary_agent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"), "Aren't bonfires fun!?")

    def test2(self):
        self.assertEqual(binary_agent("01001001 00100000 01101100 01101111 01110110 01100101 00100000 01000110 01110010 01100101 01100101 01000011 01101111 01100100 01100101 01000011 01100001 01101101 01110000 00100001"), "I love FreeCodeCamp!")


if __name__ == "__main__":
    unittest.main()


