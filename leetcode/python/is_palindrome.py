"""
### Problem ###
https://leetcode.com/problems/valid-palindrome/description/
"""

import unittest


class IsPalindromeTest(unittest.TestCase):
    def isPalindrome(self, s):
        if s == "":
            return True

        def isAlphaOrDigit(x):
            return (x.isalpha() or x.isdigit())

        chars = "".join(list(filter(isAlphaOrDigit, list(s))))

        num_words = len(chars)

        for i in range(int(num_words / 2)):
            j = num_words - i - 1
            # print(i, j, chars[i], chars[j])

            if chars[i].lower() != chars[j].lower():
                return False

        return True

    def test_basic(self):
        self.assertTrue(self.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.isPalindrome("race a car"))
