"""
### Problem ###

https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

### Notes ###

From API documentation

A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as
dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including
zero or negative counts. The Counter class is similar to bags or multisets in other languages.

"""

from collections import Counter

import unittest


class TopKFrequentElementsTest(unittest.TestCase):
    def top_k_frequent(self, nums, k):
        c = Counter()
        for n in nums:
            c[n] += 1

        return list(map(lambda x: x[0], c.most_common(k)))

    def test_example_1(self):
        self.assertEqual([1, 2], self.top_k_frequent([1, 1, 1, 2, 2, 3], 2))

    def test_example_2(self):
        self.assertEqual([1], self.top_k_frequent([1], 1))
