"""
### Problem ###
https://leetcode.com/problems/power-of-three/description/

Given an integer, write a function to determine if it is a power of three.

### Notes ###


n^3

log3(n) = log(n) / log(3)

y=log(x)
10^y = x

y=log3(x)
3^y=x



"""

import unittest


class PowerOfThreeTest(unittest.TestCase):
    def is_power_of_three(self, n):
        import math
        if n < 1 or n is None: return False
        x = math.log(n)
        y = math.log(3)
        f = int(math.ceil(x / y))

        return math.pow(3, f) == n

    def test_example_1(self):
        self.assertTrue(self.is_power_of_three(27))

    def test_example_2(self):
        self.assertFalse(self.is_power_of_three(0))

    def test_example_3(self):
        self.assertTrue(self.is_power_of_three(9))

    def test_example_4(self):
        self.assertFalse(self.is_power_of_three(45))

    def test_example_5(self):
        self.assertFalse(self.is_power_of_three(-3))

    def test_example_6(self):
        self.assertTrue(self.is_power_of_three(243))
