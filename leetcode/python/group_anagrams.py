"""
### Problem ###
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

### Notes ###

This was easy.

"""

import unittest


class GroupAnagramsTest(unittest.TestCase):
    def group_anagrams(self, strs):
        def f(x):
            index = x[0]
            original = x[1]
            sortedd = "".join(sorted(x[1]))
            return (index, original, sortedd)

        m = {}

        def g(x):
            if x[2] not in m:
                m[x[2]] = []
            m[x[2]].append(x[1])

        x = map(g, map(f, enumerate(strs)))
        list(x)

        return [v for k, v in m.items()]

    def test_example_1(self):
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]
        self.assertEqual(expected, self.group_anagrams(input))
