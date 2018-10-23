# https://leetcode.com/problems/house-robber/description/


class Solution:
    # HINT:
    # if the previous house had been robbed, we cannot rob this house
    # if the previous house not not been robbed, we can (but not must) rob this house

    def helper(self, nums, i, memo):
        num_nums = len(nums)
        last_num = num_nums - 1

        ans = 0

        if i not in memo:
            if i >= num_nums:
                ans = 0
            elif i == last_num:
                ans = nums[last_num]
            else:
                x = nums[i] + self.helper(
                    nums, i + 2,
                    memo)  # rob this house, NOT i+1, recurse from i+2
                y = nums[i + 1] + self.helper(
                    nums, i + 3,
                    memo)  # rob next house, NOT i+2, recurse from i+3
                ans = max(x, y)
            memo[i] = ans
        else:
            ans = memo[i]

        return ans

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}

        return self.helper(nums, 0, memo)
