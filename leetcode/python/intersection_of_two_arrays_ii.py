class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = set()

        dict1 = {}
        for n in nums1:
            if n not in nums:
                nums.add(n)
            if n not in dict1:
                dict1[n] = 1
            else:
                dict1[n] += 1

        dict2 = {}
        for n in nums2:
            if n not in nums:
                nums.add(n)
            if n not in dict2:
                dict2[n] = 1
            else:
                dict2[n] += 1

        ans = []
        for n in list(nums):
            if n in dict1 and n in dict2:
                for _ in range(min(dict1[n], dict2[n])):
                    ans.append(n)

        return ans

