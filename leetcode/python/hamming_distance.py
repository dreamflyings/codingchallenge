"""
### Problem ###

https://leetcode.com/problems/hamming-distance/description/

Hamming distance is the number of positions wher the corresponding bits are different.


x  y x    y    h | x ^ y
1  4 0001 0100 2   0101
0  0 0000 0000 0   0000
3  2 0011 0010 1   0001
"""

import unittest


class Solution(unittest.TestCase):
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    xor = x ^ y

    bits = 0
    while xor > 0:
      if xor & 0x1:
        bits += 1
      xor >>= 1

    return bits

  def test_smoke(self):
    self.assertEqual(2, self.hammingDistance(1, 4))
    self.assertEqual(1, self.hammingDistance(3, 2))
    self.assertEqual(0, self.hammingDistance(0, 0))

unittest.main(exit=False)

