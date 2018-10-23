"""
### Problem ###

Kth Largest Element in an Array

https://leetcode.com/problems/kth-largest-element-in-an-array/

https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/

Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

### Notes ###

sorted is O(n*logn), not the greatest solution :(

use heapq instead?

Heap is a special case of a balanced binary tree.  It is mainly used to represent a priority queue.

A pop returns the smallest element of the array (min heap).

When elements are pushed or popped, the heap structure is maintained.

its left child is located at 2*k index 
its right child is located at 2*k+1. index 
its parent is located at k/2 index

"""

import unittest

import heapq


class FindKthLargestTest(unittest.TestCase):
    def find_kth_largest(self, nums, k):
        # num_nums = len(nums)
        # return sorted(nums)[num_nums-k]
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

    def test_example_1(self):
        self.assertEqual(5, self.find_kth_largest([3, 2, 1, 5, 6, 4],
                                                  2))  # 1,2,3,4, 5,6

    def test_example_2(self):
        self.assertEqual(4,
                         self.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6],
                                               4))  # 1,2,2,3,3, 4,5,5,6
        # heapify -> [1, 2, 3, 2, 3, 4, 5, 5, 6]
