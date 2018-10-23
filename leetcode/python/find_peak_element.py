class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_nums = len(nums)

        if num_nums == 1:
            return 0

        if num_nums == 2:
            return 0 if nums[0] > nums[1] else 1

        left = 0
        right = num_nums - 1

        while right > left:
            mid = left + int((right - left) / 2)

            left_of_mid_val = nums[mid - 1] if (mid - 1) >= 0 else nums[0]
            mid_val = nums[mid]
            right_of_mid_val = nums[mid + 1] if (
                mid + 1) < num_nums else nums[num_nums - 1]

            if (right - left) == 1:
                if right_of_mid_val >= left_of_mid_val:
                    return right
                else:
                    return left

            if left_of_mid_val < mid_val and mid_val > right_of_mid_val:
                return mid

            if left_of_mid_val < mid_val:
                left = mid
            else:
                right = mid

        return None
