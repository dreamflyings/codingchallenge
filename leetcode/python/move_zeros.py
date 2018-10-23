"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
"""
nums       = 0 1 0 3 12
expected   = 1 3 12 0 0

i | num_shifts[i] num_zeros
0   0             1
1   1             1
2   1             2
3   2             2
4   2             2

i j
0 0                    0 1 0 3 12
1 0 nums[0] = nums[1]  1 1 0 3 12
2 1 nums[1] = nums[2]  1 0 0 3 12
3 1 nums[1] = nums[3]  1 3 0 3 12
4 2 nums[2] = nums[4]  1 3 12 3 12

num_nums - num_zeros = 5 -2 = 3

--

nums       = 0 1 0
num_shifts = 0 1 1
expected   = 1 0 0

i | num_shifts[i] num_zeros
0 | 0             1
1 | 1             1
2 | 1             2

j = i-num_shifts[i]

i j
0 0                   0 1 0
1 0 nums[0] = nums[1] 1 1 0
2 1 nums[1] = nums[2] 1 0 0
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_nums = len(nums)
        num_zeros = 0
        num_shifts = [0 for _ in range(num_nums)]

        for i in range(num_nums):
            num_shifts[i] = num_zeros

            if nums[i] == 0:
                num_zeros += 1
        #print(num_shifts)

        for i in range(num_nums):
            j = i - num_shifts[i]
            nums[j] = nums[i]

        #print(num_nums)
        for i in range(num_nums - num_zeros, num_nums):
            nums[i] = 0
