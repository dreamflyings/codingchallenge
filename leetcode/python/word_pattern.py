"""
https://leetcode.com/problems/word-pattern/description/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
p_to_s[a] = dog
s_to_p[dog] = a
p_to_s[b] = cat
s_to_p[cat] = b



Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains
lowercase letters separated by a single space.

"""


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        p_to_s = {}
        s_to_p = {}

        sl = str.split(" ")
        pl = list(pattern)

        if len(sl) != len(pl):
            return False

        for s, p in zip(sl, pl):
            if s not in s_to_p and p not in p_to_s:
                s_to_p[s] = p
                p_to_s[p] = s
            elif s in s_to_p and p in p_to_s:
                if s_to_p[s] != p or p_to_s[p] != s:
                    return False
            else:
                return False

        return True
