import unittest

"""
Wherefore art thou

Make a function that looks through a list of dictionaries (first argument) and 
returns a list of all dictionaries that have matching name and value pairs 
(second argument). Each name and value pair of the source dict has to be 
present in the dict from the collection if it is to be included in the returned 
list.

For example, if the first argument is [{ "first:: "Romeo", "last": "Montague" },
 { "first": "Mercutio", "last": None }, { "first": "Tybalt", "last": "Capulet" }],
and the second argument is { "last": "Capulet" }, then you must return the 
third dict from the list (the first argument), because it contains the name and 
its value that was passed on as the second argument.

"""

def what_is_in_a_name(collection, source):
    results = []
    for item in collection:
        is_ok = True
        for key in source:
            if (key not in item) or (item[key] != source[key]):
                is_ok = False
        if is_ok == True:
            results.append(item)
    return results


print(what_is_in_a_name([{ "first": "Romeo", "last": "Montague"}, 
                         { "first": "Mercutio", "last": None},
                         { "first": "Tybalt", "last": "Capulet"}],
                         {"last": "Capulet"}))


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertListEqual(what_is_in_a_name([
                         { "first": "Romeo", "last": "Montague"}, 
                         { "first": "Mercutio", "last": None},
                         { "first": "Tybalt", "last": "Capulet"}],
                         {"last": "Capulet"}), [{"first": "Tybalt", "last": "Capulet"}])

    def test2(self):
        self.assertListEqual(what_is_in_a_name([{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }], { "apple": 1 }), [{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }])
        

    def test3(self):
        self.assertListEqual(what_is_in_a_name([{ "apple": 1, "bat": 2 }, { "bat": 2 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "bat": 2 }), [{ "apple": 1, "bat": 2 }, { "apple": 1, "bat": 2, "cookie": 2 }])

    def test4(self):
        self.assertListEqual(what_is_in_a_name([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "cookie": 2 }), [{"apple": 1, "bat": 2, "cookie": 2}])

    def test5(self):
        self.assertListEqual(what_is_in_a_name([{"a": 1, "b": 2, "c": 3}], {"a": 1, "b": 9999, "c": 3}), [])

    def test6(self):
        self.assertListEqual(what_is_in_a_name([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }, { "bat":2 }], { "apple": 1, "bat": 2 }), [{ "apple": 1, "bat": 2 }, { "apple": 1, "bat": 2, "cookie":2 }])

    def test7(self):
        self.assertListEqual(what_is_in_a_name([{"a": 1, "b": 2, "c": 3, "d": 9999}], {"a": 1, "b": 9999, "c": 3}), [])



if __name__ == "__main__":
    unittest.main()
