"""
### Problem ###

https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/

Given an array with n objects colored red, white or blue, sort them in-place so
that objects of the same color are adjacent, with the colors in the order red,
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.

- First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
  array with total number of 0's, then 1's and followed by 2's.

- Could you come up with a one-pass algorithm using only constant space

### Notes ###

Two pass algorithm is easy.  It is described above.

MARK index OF last ONE

i nums nums[i] l nums' l'
0 120  1       - 120   0 # mark index of last one
1 120  2       0 120   0 # pop 2, insert after last one
2 120  0       1 012     # pop 0, insert at head, l++

Input:  [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


i nums    nums[i]  l | nums'   l'
0 202110  2       -1 | 202110  -1
1 202110  0       -1 | 022110  -1
2         2
3         1
4         1
5         0

Input: [1,2,1]
Output: [1,1,2]


i nums num l | nums' l'
0 121  1   0   121   0  before first one   -> pop(0), insert(0, 1)
1 121  2       121   1  insert after first one -> pop(1), insert(0, 2)
2 121  1       112      insert before after one -> pop(1), insert(0, 1), l++


Input: [1,2,0]
Output: [0,1,2]

i nums num l | nums' l'
0 120  1   0 | 120   0 before first one -> pop(0), insert(0, 1) // index of insert <= i
1 120  2     | 120   0 after first one -> pop(1), insert(0, 2)
2 120  0     |         at heat -> pop(0), insert(0,0

"""

import unittest


class SortColorsTest(unittest.TestCase):
    def sort_colors(self, nums):
        i = 0
        l = 0

        while i < len(nums):
            num = nums[i]
            is_zero = num == 0
            is_one = num == 1
            is_two = num == 2

            nums.pop(i)

            if is_zero:
                # insert at head
                nums.insert(0, 0)
                l += 1
            elif is_two:
                # insert after first one
                nums.insert(l, 2)
            elif is_one:
                # insert after first one
                nums.insert(l, 1)
                l += 1

            i += 1
        return nums

    def test_basic(self):
        self.assertEqual([0, 0, 1, 1, 2, 2], self.sort_colors([2, 0, 2, 1, 1, 0]))

    def test_corner_2(self):
        self.assertEqual([0, 1, 2], self.sort_colors([1, 2, 0]))

    def test_corner_2(self):
        self.assertEqual([1, 1, 2], self.sort_colors([1, 2, 1]))
