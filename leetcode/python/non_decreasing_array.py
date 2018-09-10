### Problem ###
# https://leetcode.com/problems/non-decreasing-array/description/

class Solution(object):
    def checkPossibility(self, nums):
        nums_count = len(nums)

        if nums_count >=0 and nums_count <= 2:
            return True

        is_greater_than = list(filter(lambda x: x == True, [ nums[i] > nums[i+1]  for i in range(len(nums)-1) ]))
        is_greater_than_count = len(is_greater_than)

        is_greater_than_by_two = list(filter(lambda x: x == True, [ nums[i] > nums[i+2]  for i in range(len(nums)-2) ]))
        is_greater_than_by_two_count = len(is_greater_than_by_two)

        if is_greater_than_count > 1 or is_greater_than_by_two_count > 1:
            return False

        return True

