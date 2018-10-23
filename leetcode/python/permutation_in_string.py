"""
# https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, write a function to return true if s2 contains the
permutation of s1. In other words, one of the first string's permutations is
the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""

# O(n!), Time Limit Exceeded :(
# import itertools
# for p in itertools.permutations(list(s1)):
#     if "".join(p) in s2:
#         return True
# return False

# O(n^2), Time Limit Exceeded :(


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1set = set(list(s1))
        s1len = len(s1)
        s2len = len(s2)

        s1map = {}
        for char in s1:
            if char not in s1map:
                s1map[char] = 1
            else:
                s1map[char] += 1

        s2list = ["" for _ in range(s1len - 1)] + list(
            s2) + ["" for _ in range(s1len - 1)]

        #print(s1map)
        #print(s2list)

        for i in range(len(s2list)):
            #print(i, i+s1len, s2list[i:i+s1len])
            window = {}
            for char in s2list[i:i + s1len]:
                if char in s1set:
                    if char not in window:
                        window[char] = 1
                    else:
                        window[char] += 1
                    if window == s1map:
                        return True
        return False
