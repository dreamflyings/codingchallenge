"""
### Problem ###
https://leetcode.com/problems/custom-sort-string/description/

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that
S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.


Example :

Input:
S = "cba"
T = "abcd" <-- permute characters of T, such that they match the order in which S were sorted

Output: "cbad"

Explanation:

"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".

Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

"""

import unittest


class CustomSortStringTest(unittest.TestCase):
    def customSortString(self, S, T):
        order = {S[i]: i for i in range(len(S))}
        z = sorted(list(T), key=lambda x: order[x] if x in order else -1)
        return "".join(z)

    def test_basic(self):
        self.assertEqual("dcba", self.customSortString("cba", "abcd"))
        self.assertEqual("dcba", self.customSortString("cbafg", "abcd"))
        self.assertEqual("kqeep", self.customSortString("kqep", "pekeq"))
