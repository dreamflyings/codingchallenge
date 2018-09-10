"""
### Problem ###
https://leetcode.com/problems/reverse-bits/description/
"""

import unittest


class Solution(unittest.TestCase):
  def reverseBits(self, n):
    bitstring = [ bit for bit in str(bin(n))[2:] ]
    bitstring_length = len(bitstring)

    if bitstring_length < 32:
      num_zeros_to_pad = 32 - bitstring_length
      bitstring = [ "0" for _ in range(num_zeros_to_pad) ] + bitstring

    bitstring.reverse()

    result = int("".join(bitstring), 2)
    return result

  def test_basic(self):
    self.assertEqual(1342177280, self.reverseBits(0xA))
    self.assertEqual(0, self.reverseBits(0))
    self.assertEqual(964176192, self.reverseBits(43261596))

unittest.main(exit=False)

