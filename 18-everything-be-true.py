import unittest

"""
Everything Be True

Check if the predicate (second argument) is truthy on all elements of 
a collection (first argument).

In other words, you are given a list collection of dictionaries. The predicate 
pre will be a dictionary property and you need to return true if its value is 
truthy. Otherwise, return false.

"""

def truth_check(collection, pre):
    return pre

print(truth_check([{"name": "Quincy", "role": "Founder", "isBot": False}, 
                   {"name": "Naomi", "role": "", "isBot": False}, 
                   {"name": "Camperbot", "role": "Bot", "isBot": True}], 
                   "isBot"))


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(truth_check([{"name": "Quincy", "role": "Founder", "isBot": False}, 
                   {"name": "Naomi", "role": "", "isBot": False}, 
                   {"name": "Camperbot", "role": "Bot", "isBot": True}], 
                   "isBot"), False)

    def test2(self):
        self.assertEqual(truth_check([{"name": "Quincy", "role": "Founder", "isBot": False}, 
                   {"name": "Naomi", "role": "", "isBot": False}, 
                   {"name": "Camperbot", "role": "Bot", "isBot": True}], 
                   "name"), True)

    def test3(self):
        self.assertEqual(truth_check([{"name": "Quincy", "role": "Founder", "isBot": False}, 
                   {"name": "Naomi", "role": "", "isBot": False}, 
                   {"name": "Camperbot", "role": "Bot", "isBot": True}], 
                   "role"), False)

    def test4(self):
        self.assertEqual(truth_check([{"name": "Pikachu", "number": 25, "caught": 3}, 
                   {"name": "Togepi", "number": 175, "caught": 1}], 
                   "number"), True)

    def test5(self):
        self.assertEqual(truth_check([{"name": "Pikachu", "number": 25, "caught": 3}, 
                   {"name": "Togepi", "number": 175, "caught": 1},
                   {"name": "MissingNo", "number": None, "caught": 0 }], 
                   "caught"), False)

    def test6(self):
        self.assertEqual(truth_check([{"name": "Pikachu", "number": 25, "caught": 3}, 
                   {"name": "Togepi", "number": 175, "caught": 1},
                   {"name": "MissingNo", "number": None, "caught": 0 }], 
                   "number"), False)

    def test7(self):
        self.assertEqual(truth_check([{"name": "Quincy", "username": "QuincyLarson"}, 
                   {"name": "Naomi", "username": "nhcarrigan"}, 
                   {"name": "Camperbot"}], 
                   "username"), False)

    def test8(self):
        self.assertEqual(truth_check([{"name": "freeCodeCamp", "users": [{"name": "Quincy"}, {"name": "Naomi"}]}, 
                                      {"name": "Code Radio", "users": [{"name": "Camperbot"}]}, 
                                      {"name": "", "users": []}], 
                   "users"), False)

    def test9(self):
        self.assertEqual(truth_check([{"id": 1, "data": {"url": "https://freecodecamp.org", "name": "freeCodeCamp"}},
                                      {"id": 2, "data": {"url": "https://coderadio.freecodecamp.org/", "name": "CodeRadio"}}, 
                                      {"id": None, "data": {}}],
                                     "data"), False)


if __name__ == "__main__":
    unittest.main()


