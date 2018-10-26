"""
https://leetcode.com/problems/majority-element/description/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

---

This appears to be straightforward?

"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        l = len(nums)
        m = -sys.maxsize
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > (l // 2):
                m = max(m, num)

        return m
