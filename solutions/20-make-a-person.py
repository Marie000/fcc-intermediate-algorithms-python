import unittest

"""
Make a Person

Create a class with only two attributes: _first_name and _last_name.

From that attribute, create properties that can be accessed or set with:
.first_name
.last_name
.full_name
hint: you will need to use the @property decorator.


"""

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    @full_name.setter
    def full_name(self, full_name):
        self._first_name = full_name.split(" ")[0]
        self._last_name = full_name.split(" ")[1]
    



"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def setUp(self):
        self.max = Person("Max", "Power")

    def test1(self):
        self.assertEqual(len(self.max.__dict__), 2, "Person should only have 2 attributes")

    def test2(self):
        self.assertIn("_first_name", self.max.__dict__, "Person should contain attribute '_first_name'")
   
    def test3(self):
        self.assertIn("_last_name", self.max.__dict__, "Person should contain attribute '_last_name'")

    def test4(self):
        self.assertEqual(self.max.first_name, "Max", "Should be able to get the first name with property .first_name")

    def test5(self):
        self.assertEqual(self.max.last_name, "Power", "Should be able to get the last name with property .last_name")

    def test6(self):
        self.assertEqual(self.max.full_name, "Max Power", "Should be able to get the full name with the property .full_name")

    def test7(self):
        self.max.first_name = "Maxim"
        self.assertEqual(self.max.first_name, "Maxim", "We should be able to set the first name with the .first_name property")

    def test8(self):
        self.max.last_name = "Power!!!!"
        self.assertEqual(self.max.last_name, "Power!!!!", "We should be able to set the last name with the .last_name property")

    def test9(self):
        self.max.full_name = "Homer Simpson"
        self.assertEqual(self.max.first_name, "Homer", "We should be able to set the first name, last name and full name with the .full_name property")
        self.assertEqual(self.max.last_name, "Simpson", "We should be able to set the first name, last name and full name with the .full_name property")
        self.assertEqual(self.max.full_name, "Homer Simpson", "We should be able to set the first name, last name and full name with the .full_name property")

if __name__ == "__main__":
    unittest.main()



