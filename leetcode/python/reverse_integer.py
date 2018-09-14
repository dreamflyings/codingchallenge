"""
### Problem ###
https://leetcode.com/problems/reverse-integer/description/

### Notes ###
I did not consider the overflow case.

"""


class ReverseInteger(object):
    def reverse(self, x):
        is_negative = True if x < 0 else False
        x = -x if is_negative else x

        result = 0

        while x != 0:
            mod = x % 10
            # FIXME: predict overflow
            result = result * 10 + mod
            x = int(x / 10)

        return -result if is_negative else result
