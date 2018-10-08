# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ["".join(reversed(w)) for w in reversed(s.split(" "))]
        return " ".join(ans)
