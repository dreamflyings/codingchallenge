"""
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.

---

egg
add

sm[e] = a
tm[a] = e

sm[g] = d
tm[d] = g

sm[g] == d
tm[d] == g
"""


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sm = {}
        tm = {}

        for ss, tt in zip(s, t):
            #print(ss, sm, tt, tm)
            if ss not in sm and tt not in tm:
                sm[ss] = tt
                tm[tt] = ss
            elif ss in sm and tt in tm:
                if sm[ss] != tt or tm[tt] != ss:
                    return False
            else:
                return False

        return True
