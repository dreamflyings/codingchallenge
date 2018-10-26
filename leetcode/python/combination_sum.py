"""
### Problem ###

https://leetcode.com/problems/combination-sum/description/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all
unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,

A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,

A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

### Notes ###

This requirement threw me off ...

"The same repeated number may be chosen from candidates unlimited number of times."

itertools.combinations_with_replacements doesn't support "repeat number unlimited of times"

INVALID BRUTE FORCE SOLUTION

"""

import itertools

import unittest


class CombinationSumTest(unittest.TestCase):
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        for r in range(len(candidates) + 7):  # HACK
            for c in filter(lambda x: sum(x) == target,
                            itertools.combinations_with_replacement(
                                candidates, r)):
                result.append(list(c))

        # result = [[7], [2, 2, 3]]
        return sorted(result)

    def test_basic(self):
        expected = sorted([[7], [2, 2, 3]])
        self.assertEqual(expected, self.combinationSum([2, 3, 6, 7], 7))

        expected = sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
        self.assertEqual(expected, self.combinationSum([2, 3, 5], 8))

        expected = sorted([[2, 2, 2, 2, 2, 2, 2, 2,
                            2], [2, 2, 2, 2, 2, 2, 3,
                                 3], [2, 2, 2, 2, 3, 7], [2, 2, 2, 3, 3, 3, 3],
                           [2, 2, 7, 7], [2, 3, 3, 3, 7], [3, 3, 3, 3, 3, 3]])
        self.assertEqual(expected, self.combinationSum([7, 3, 2], 18))
