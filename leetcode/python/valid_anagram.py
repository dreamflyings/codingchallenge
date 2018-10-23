# Problem: https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counts = {}
        for s_ch in s:
            if s_ch not in s_counts: s_counts[s_ch] = 1
            else: s_counts[s_ch] += 1

        t_counts = {}
        for t_ch in t:
            if t_ch not in t_counts: t_counts[t_ch] = 1
            else: t_counts[t_ch] += 1

        return True if s_counts == t_counts else False
