"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Given a string s and a non-empty string p, find all the start indices of p's
anagrams in s.

Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

---

This was a very good question, not easy imho.

"""


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        slen = len(s)

        plen = len(p)

        pcounts = {}
        for pchar in p:
            pcounts[pchar] = pcounts.get(pchar, 0) + 1

        if plen > slen: return []
        """
        pcounts = {a:1, b:1, c:1}
        cbaebabacd
        scounts_init = {c:1,b:1,a:1}

        i j   range notes
        0 3   0 1 2 remove 0 add j
        1 4   1 2 3
        2 5
        [..]
        7 10
        """

        scounts = {}
        for x in range(plen):
            scounts[s[x]] = scounts.get(s[x], 0) + 1

        indices = []
        i = 0
        j = plen

        while j <= slen:  # <= because range is non inclusive
            #print(i, j, s[i:j], slen, pcounts, scounts)
            if pcounts == scounts:
                indices.append(i)

            scounts[s[i]] -= 1  # remove left
            if scounts[s[i]] == 0:
                del scounts[s[i]]

            if j < slen:
                scounts[s[j]] = scounts.get(s[j], 0) + 1  # add right

            i += 1
            j += 1

        return indices
