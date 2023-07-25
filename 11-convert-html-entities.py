import unittest

"""
Convert HTML Entities

Convert the characters &, <, >, " (double quote), and ' (apostrophe), 
in a string to their corresponding HTML entities.

hint:
HTML_ENTITIES = {
    "&": "&amp;",
    ">": "&gt;",
    "<": "&lt;",
    '"': "&quot;",
    "'": "&apos;"
}

"""

def convert_html(string):
    return string

print(convert_html("Dolce & Gabbana"))

"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(convert_html("Dolce & Gabbana"), "Dolce &amp; Gabbana")

    def test2(self):
        self.assertEqual(convert_html("Hamburgers < Pizza < Tacos"), "Hamburgers &lt; Pizza &lt; Tacos")

    def test3(self):
        self.assertEqual(convert_html("Sixty > twelve"), "Sixty &gt; twelve")

    def test4(self):
        self.assertEqual(convert_html('Stuff in "quotation marks"'), "Stuff in &quot;quotation marks&quot;")

    def test5(self):
        self.assertEqual(convert_html("Schindler's List"), "Schindler&apos;s List")

    def test6(self):
        self.assertEqual(convert_html("<>"), "&lt;&gt;")

    def test7(self):
        self.assertEqual(convert_html("abc"), "abc")

if __name__ == "__main__":
    unittest.main()