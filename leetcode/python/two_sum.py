"""
### Problem ###

https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

### Notes ###

I only came up with the brute force approach myself.  The idea behind the O(1) approach is to consider the complement
of the sum.

nums[i] + nums[j] = target

for i in range(len(nums)):
    left = nums[i]
    right = target - nums[i] # <-- this may have been previously computed, use right to index map to return index where
                             # it was computed
"""

import unittest


class TwoSumTest(unittest.TestCase):
    # brute force approach, O(n^2)
    #
    #    def twoSum(self, nums, target):
    #        l = len(nums)
    #        for (i, j, sum) in [(i, j, nums[i] + nums[j]) for i in range(l) for j in range(i+1, l) if i != j]:
    #            if sum == target:
    #                return [i, j]
    #        raise ValueError("illegal input")

    def twoSum(self, nums, target):
        complement_index = {}
        for i in range(len(nums)):
            x = nums[i]
            xp = target - x  # complement

            if x in complement_index:
                return sorted([i, complement_index[x]])
            else:
                complement_index[xp] = i

        raise ValueError("illegal input")

    def test_basic(self):
        self.assertEqual(self.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.twoSum([3, 2, 4], 6), [1, 2])
