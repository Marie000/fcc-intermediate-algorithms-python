import unittest

"""
Map the Debris

According to Kepler's Third Law, the orbital period T of two point masses orbiting each other in a circular or elliptic orbit is:

T=2π * square root of (a**3 / μ) (see https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/map-the-debris )

a is the orbit's semi-major axis
μ=GM is the standard gravitational parameter
G  is the gravitational constant,
M  is the mass of the more massive body.

Return a new list that transforms the elements' average altitude into their orbital 
periods (in seconds).

The list will contain dictionaries in the format {"name": "name", "avg_alt": avg_alt}.
The returned list will contain dictionaries with the format {"name": "name", "orbital_period": orbital_period}

The values should be rounded to the nearest whole number. The body being orbited is 
Earth.

The radius of the earth is 6367.4447 kilometers, and the GM value of earth is 
398600.4418 km3s-2.

"""

import math

def orbital_period(list):
    GM = 398600.4418
    EARTH_RADIUS = 6367.4447
    results = []
    for sattelite in list:
        semi_major_axis = EARTH_RADIUS + sattelite["avg_alt"]
        orbital_period = 2 * math.pi * (math.sqrt((semi_major_axis ** 3) / GM))
        results.append({"name": sattelite["name"], "orbital_period": round(orbital_period)})

    return results

print(orbital_period([{"name": "sputnik", "avg_alt": 35873.5553}]))




"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class Tests(unittest.TestCase):

    def test1(self):
        self.assertListEqual(orbital_period([{"name" : "sputnik", "avg_alt" : 35873.5553}]), 
                             [{"name": "sputnik", "orbital_period": 86400}])

    def test2(self):
        self.assertListEqual(orbital_period([{"name" : "iss", "avg_alt" : 413.6}, 
                                             {"name": "hubble", "avg_alt": 556.7}, 
                                             {"name": "moon", "avg_alt": 378632.553}]), 
                                             [{"name" : "iss", "orbital_period": 5557}, 
                                              {"name": "hubble", "orbital_period": 5734}, 
                                              {"name": "moon", "orbital_period": 2377399}])


if __name__ == "__main__":
    unittest.main()

