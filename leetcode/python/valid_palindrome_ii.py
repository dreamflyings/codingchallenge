"""
### Problem ###
https://leetcode.com/problems/valid-palindrome-ii/description/
"""

import unittest


class Solution(unittest.TestCase):
  def isPalindrome(self, s):
    num_chars = len(s)

    if num_chars == 0 or num_chars == 1:
      return False

    for i in range(int(num_chars/2)):
      j = num_chars - i - 1

      if s[i] != s[j]:
        return False
    return True

  def validPalindrome(self, s):
    num_chars = len(s)

    if num_chars >= 0 and num_chars <= 2:
      return True

    for i in range(int(num_chars/2)):
      j = num_chars - i - 1

      if s[i] != s[j]:
        # delete i # FIXME: DNR
        ssl = "" if i-1 < 0 else s[0:i]
        ssr = "" if i+1 == num_chars else s[i+1:]
        ss = ssl + ssr
        if self.isPalindrome(ss): return True

        # delete j # FIXME: DNR
        ssl = "" if j-1 < 0 else s[0:j]
        ssr = "" if j+1 == num_chars else s[j+1:]
        ss = ssl + ssr
        if self.isPalindrome(ss): return True

        return False

    return True

  def test_basic(self):
    self.assertTrue(self.validPalindrome("aa"))
    self.assertTrue(self.validPalindrome("yd"))
    self.assertTrue(self.validPalindrome("aba"))
    self.assertTrue(self.validPalindrome("abca"))
    self.assertTrue(self.validPalindrome("zabcaz"))
    self.assertFalse(self.validPalindrome("abc"))
    self.assertTrue(self.validPalindrome("deeee"))
    self.assertTrue(self.validPalindrome("eeeed"))
    self.assertTrue(self.validPalindrome("eedede"))

unittest.main(exit=False)

