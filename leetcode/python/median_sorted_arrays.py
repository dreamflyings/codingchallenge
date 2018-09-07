"""
### Problem ###

https://leetcode.com/problems/median-of-two-sorted-arrays/description/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

### Notes ###

My algorithm's complexity is O(n), not O(log(m+n).

[1,2] [3,4] => [1,2,3,4], median index = 2-1, 3-1, (result[1]+result[2])/2.0 median = 2 + 3 /2 = 2.3
[1,3] [2] => [1,2,3], median index = 2 -> 2-1 (result[1] = 2.0)
"""

import unittest


class MedianSortedArrayTest(unittest.TestCase):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        num_points = nums1_len + nums2_len

        result = []

        for x in range(num_points):
            nums1_i = nums1[i] if i < nums1_len else None
            nums2_j = nums2[j] if j < nums2_len else None

            if nums1_i is not None and nums2_j is not None:
                if nums1_i <= nums2_j:
                    result.append(nums1_i)
                    i += 1
                else:
                    result.append(nums2_j)
                    j += 1
            elif nums1_i is not None and nums2_j is None:
                result.append(nums1_i)
                i += 1
            elif nums1_i is None and nums2_j is not None:
                result.append(nums2_j)
                j += 1
            else:
                raise ValueError("Illegal input")

        if num_points % 2 == 0:
            index_even = int(num_points / 2)
            return (result[index_even-1] + result[index_even]) / 2.0
        else:
            index_odd = int((num_points - 1) / 2)
            return float(result[index_odd])

    def test_basic(self):
        self.assertEqual(self.findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(self.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(self.findMedianSortedArrays([2], []), 2.0)
