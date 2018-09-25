"""
### Problem ###

https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Notes ###

I hacked at this one for _two_ hours.  I was very close, but the solution was messy.  I then decided to look at the
solution.

Two pointers, i, j.

j is ahead pointer, adds chars to set if they do not exist, remove if they do.  answer is the maximum size of the set

abcabcbb

j i set
0
1
2   abc | ab | max = 3
3 1     | b
4         b
5
6





"""

import unittest


class LengthOfLongestSubstringTest(unittest.TestCase):
    def length_of_longest_substring(self, s):
        if s == "": return 0

        n = len(s)
        substr = set()
        result = 0
        i = 0
        j = 0

        while i < n and j < n:
            # print("i", i)
            # print("j", j)
            # print("substr", substr)

            si = s[i]
            sj = s[j]
            if not s[j] in substr:
                substr.add(sj)
                j += 1
                if (j - i) > result:
                    result = j - i
            else:
                substr.remove(si)
                i += 1

        return result

    def test_example_1(self):
        self.assertEqual(3, self.length_of_longest_substring("abcabcbb"))

    def test_example_2(self):
        self.assertEqual(1, self.length_of_longest_substring("bbbbb"))

    def test_example_3(self):
        self.assertEqual(3, self.length_of_longest_substring("pwwkew"))

    def test_example_4(self):
        self.assertEqual(2, self.length_of_longest_substring("au"))

    def test_example_5(self):
        self.assertEqual(2, self.length_of_longest_substring("aab"))

    def test_example_6(self):
        self.assertEqual(3, self.length_of_longest_substring("dvdf"))

    def test_bounds_1(self):
        self.assertEqual(1, self.length_of_longest_substring(" "))

    def test_bounds_2(self):
        self.assertEqual(0, self.length_of_longest_substring(""))
