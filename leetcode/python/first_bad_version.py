"""
### Problem ###
https://leetcode.com/problems/first-bad-version/description/

"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            m = l + int((r-l)/2)
            if isBadVersion(m):
                r = m
            else:
                l = m+1 # l += 1
        return l