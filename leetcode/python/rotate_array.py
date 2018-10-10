# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_nums = len(nums)

        if num_nums == 1 or num_nums == 0 or k == 0:
            return

# Time Limit Exceeded
#        for i in range(k % num_nums):
#            tmp = nums[num_nums-1]
#            for j in reversed(range(1, num_nums)):
#                nums[j] = nums[j-1]
#            nums[0] = tmp

        k = k % num_nums
        nk = num_nums - k # 7 - 3 = 4
        #print(nums[nk:]) # [4:6] -> [5, 6, 7]
        #print(nums[:nk]) # [0:4-1] -> [1, 2, 3, 4]

        #nums = nums[nk:] + nums[:nk] # nope, not inplace
        nums[:] = nums[nk:] + nums[:nk]

