"""
https://leetcode.com/problems/reverse-string-ii/description/

Given a string and an integer k, you need to reverse the first k characters for
every 2k characters counting from the start of the string. If there are less
than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and
left the other as the original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
---
abcdefg k = 2
ab cd ef g
2k 0,2,4,[..]

r i j
t 0k  0k:1k
f 1k  1k:2k
t 2k  2k:3k

r i j
t 0 0:2
f 2 2:4
t 4 4:6
"""

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        reverse = True
        l = []
        i = 0

        while i < len(s):
            tmp = s[i*k:(i+1)*k]
            if reverse
                tmp = tmp[::-1]
            l.append(tmp)
            reverse = not reverse
            i += 1

        return "".join(l)

