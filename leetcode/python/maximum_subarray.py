"""
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle

### Notes ###

* I think this is a sliding window problem.
* Maintain a subarray <--- no this is too complicated
* Look at possibilities when moving to next
- append to head
- remove from tail

Input: [-2,1,-3,4,-1,2,1,-5,4]

max_sum = -2
cur_sum = -2 <--- maintain count of the current sum, but RESET if number if bigger

     cur_sum
     max(num, cur_sum + num[i])
1    max(1, 1-2)= 1
-3   max(-3, -3+1) = -2
4    max(4, 4-2) = 4
-1   max(-1, -1+4) = 3
2    max(2, 2+3) = 5
1    max(1, 1+5)  = 6 <---
-5   max(-5,-5+6) = 1
4    max(4, 1+4) = 4

"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_nums = len(nums)

        if num_nums == 0:
            return 0
        elif num_nums == 1:
            return nums[0]

        cur_sum = nums[0]
        max_sum = nums[0]
        i = 1

        while i < num_nums:
            cur_sum = max(nums[i] + cur_sum, nums[i])
            max_sum = max(max_sum, cur_sum)
            i += 1

        return max_sum
