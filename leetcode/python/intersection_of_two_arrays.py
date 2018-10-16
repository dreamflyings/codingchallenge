class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        ans = list(set1.intersection(set2))
        return ans

