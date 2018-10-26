"""
### Problem ###

http://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

### Notes ###

This wasn't very complicated, but required trial and error on my part.

"""

import unittest


class RemoveDuplicatesSortedArrayTest(unittest.TestCase):
    def removeDuplicates(self, nums):
        if nums == []: return 0

        num_swaps = 0

        tail_ptr = 0
        head_ptr = 1

        while head_ptr < len(nums):
            tail_val = nums[tail_ptr]
            head_val = nums[head_ptr]

            if tail_val == head_val:
                head_ptr += 1
            else:
                tail_ptr += 1
                nums[tail_ptr] = nums[head_ptr]
                num_swaps += 1

        return num_swaps + 1

    def test_basic(self):
        self.assertEqual(self.removeDuplicates([]), 0)
        self.assertEqual(self.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(
            self.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(self.removeDuplicates([0, 0, 4]), 2)
        self.assertEqual(self.removeDuplicates([0, 0, 4, 5, 6, 7]), 5)
        self.assertEqual(5,
                         self.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3,
                                                4]))  # [0, 1, 2, 3, 4]
