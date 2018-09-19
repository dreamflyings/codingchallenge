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

Input:  [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

i nums    nums[i] action
0 [1,2,0] 1       -
1 [1,2,0] 2       move to back
1 [1,0,2] 0       move to front
2 [0,1,2] end, do nothing 


[1, 2, 0] 0 False False

[1, 2, 0] 1 False True
[1, 0, 2] 1 True False

[0, 1, 2] 2 False True
[0, 1, 2] 2 False True


MARK the LAST zero



i nums l nums' l'
0 120  0 120   0
1 120  0 120   1
2 120  1 012

1 2 0 l=0
2 1 0 l++






"""

import unittest


class SortColorsTest(unittest.TestCase):
    def sort_colors(self, nums):
        i = 0
        while i < len(nums)-1:
            num = nums[i]
            is_zero = num == 0
            is_two = num == 2
            print(nums, i, is_zero, is_two)

            if is_zero:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            elif is_two:
                nums.pop(i)
                nums.append(2)
            else:
                i += 1
        return nums

             

    def test_basic(self):
        self.assertEqual([0,0,1,1,2,2], self.sort_colors([2,0,2,1,1,0]))

    def test_corner(self):
        self.assertEqual([0,1,2], self.sort_colors([1,2,0]))

