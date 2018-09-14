"""
### Problem ###

https://leetcode.com/problems/jewels-and-stones/description/

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

### Notes ###

Remember O(n^2) or brute force shouldn't be considered ....

Just use a set()

"""

import unittest


class JewelsAndStonesTest(unittest.TestCase):
    def numJewelsInStones(self, J, S):
        jewels = set(list(J))
        return sum([1 for stone in list(S) if stone in jewels])

    def test_smoke(self):
        self.assertEqual(3, self.numJewelsInStones("aA", "aAAbbbb"))
        self.assertEqual(0, self.numJewelsInStones("z", "ZZ"))
