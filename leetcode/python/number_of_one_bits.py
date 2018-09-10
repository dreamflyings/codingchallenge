"""
### Problem ###
https://leetcode.com/problems/number-of-1-bits/description/
"""

import unittest


class Solution(unittest.TestCase):
  def hammingWeight(self, n):
    onesCount = 0

    while n > 0:
      if n & 0x1:
        onesCount += 1
      n = n >> 1

    return onesCount

  def test_basic(self):
    self.assertEqual(1, self.hammingWeight(2))
    self.assertEqual(3, self.hammingWeight(11))
    self.assertEqual(0, self.hammingWeight(0))
    self.assertEqual(1, self.hammingWeight(128))

unittest.main(exit=False)

