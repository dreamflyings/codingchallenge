# https://leetcode.com/problems/first-unique-character-in-a-string/description/

from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        d = OrderedDict()

        pos = 0
        for c in s:
            if not c in d:
                d[c] = (0, pos)
            else:
                d[c] = (d[c][0] + 1, pos)
            pos += 1

        for k, v in d.items():
            if d[k][0] == 0:
                return d[k][1]

        return -1
