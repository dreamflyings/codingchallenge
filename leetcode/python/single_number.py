### Problem ###
# https://leetcode.com/problems/single-number/description/

### Notes ###

# This is a stupid trick question. Consider properties of xor:
#
# A^A = 0
# A^0 = A
# 0^0 = 0
# 1^1 = 0
# A^B = B^A
# A^(B^C)=(A^B)^C # commutative
#
# 221
# 2^2^1=0^1=1
#
# 41212
# (1^1)^(2^2)^4
# (0)^(0)^4 = 4


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans
