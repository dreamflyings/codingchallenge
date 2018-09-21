"""
### Problem ###
https://leetcode.com/problems/divide-two-integers/description/

### Notes ###

Is it a simple loop?

# dividend_is_neg = dividend < 0
# divisor_is_neg = divisor < 0
#
# is_neg = dividend_is_neg ^ divisor_is_neg
#
# dividend = -dividend if dividend_is_neg else dividend
# divisor = -divisor if divisor_is_neg else divisor
#
# count = 0
#
# while True:
#     dividend -= divisor
#     if dividend < 0:
#         break
#     count += 1
#
# return -count if is_neg else count

... NOPE, use bit manipulation to find quotient

"""

import unittest


class DivideTwoIntegersTest(unittest.TestCase):
    def divide(self, dividend, divisor):
        dividend_is_neg = dividend < 0
        divisor_is_neg = divisor < 0

        is_neg = dividend_is_neg ^ divisor_is_neg

        dividend = -dividend if dividend_is_neg else dividend
        divisor = -divisor if divisor_is_neg else divisor

        count = 0

        while True:
            dividend -= divisor
            if dividend < 0:
                break
            count += 1

        return -count if is_neg else count

    def test_example_1(self):
        self.assertEqual(6, self.divide(20, 3))

    def test_example_2(self):
        self.assertEqual(-2, self.divide(7, -3))
