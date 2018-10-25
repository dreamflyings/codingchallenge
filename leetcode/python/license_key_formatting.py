"""
https://leetcode.com/problems/license-key-formatting/description/
"""


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = list(filter(lambda x: x != '-', list(S)))[::-1]
        l = len(s)
        r = []

        for i in range(l):
            r.append(s[i].upper())
            if i % K == K - 1 and i != l - 1:
                r.append('-')

        return "".join(r[::-1])
