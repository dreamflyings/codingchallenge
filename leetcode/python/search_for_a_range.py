"""
### Problem ###

https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

### Notes ###

This appears to be a binary search problem.

[5, 7, 7, 8, 8, 10]
 0  1  2  3  4  5


l  r  m  val
0  5  2  5 < 8, go right
3  5  4  8,     found!


left search
l  r  m  v
0  3  2  7 < 8

- first, see if I can a binary search right
- then, search left
- then, search right

"""

import unittest


class SearchForARangeTest(unittest.TestCase):
    def search(self, nums, left, right, target):
        mid = int(left + (right - left) / 2)
        val = nums[mid]

        if target == val:
            return mid
        elif val < target and right >= mid + 1:
            return self.search(nums, mid + 1, right, target)
        elif val > target and mid - 1 >= left:
            return self.search(nums, left, mid - 1, target)
        else:
            return -1

    def search_range(self, nums, target):
        if not nums: return [-1, -1]

        num_nums = len(nums)

        mid = self.search(nums, 0, num_nums - 1, target)

        if mid == -1: return [-1, -1]

        mid_is_zero = mid == 0
        mid_is_max = mid == num_nums - 1

        if mid_is_max and mid_is_zero: return [0, 0]

        # search left
        l = 0
        if not mid_is_zero:
            l = mid
            while l > 0:
                if l == 0:
                    if nums[0] != target:
                        l = -1
                    break
                else:
                    if nums[l - 1] == target:
                        l -= 1
                    else:
                        break

        # search right
        r = num_nums - 1
        if not mid_is_max:
            r = mid
            while r < num_nums - 1:
                if r == num_nums - 1:
                    if nums[num_nums - 1] != target:
                        r += 1
                    break
                else:
                    if nums[r + 1] == target:
                        r += 1
                    else:
                        break

        return [l, r]

    def test_example_1(self):
        self.assertEqual([3, 4], self.search_range([5, 7, 7, 8, 8, 10], 8))

    def test_example_2(self):
        self.assertEqual([-1, -1], self.search_range([5, 7, 7, 8, 8, 10], 6))

    def test_example_3(self):
        self.assertEqual([0, 0], self.search_range([1], 1))

    def test_example_4(self):
        self.assertEqual([0, 1], self.search_range([2, 2], 2))

    def test_example_5(self):
        self.assertEqual([1, 1], self.search_range([1, 4], 4))

    def test_example_6(self):
        self.assertEqual([0, 2], self.search_range([0, 0, 0, 1, 2, 3], 0))

    def test_bounds_1(self):
        self.assertEqual([-1, -1], self.search_range([], 0))
