"""
### Problem ###

https://leetcode.com/problems/largest-number/description/

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.

### Notes ###

Here was my initial incorrect solution.

''.join(sorted(map(str, nums), key = lambda x: x[:1], reverse=True))

I thought of some brute force solutions, but needed hints from the solution :( and python docs:

key parameter specifies a function to be called on each list element prior to making comparaisons.  The value
of key parameter should be a function that takes a simple argument and returns a key for sorting purposes.

sort routines are GUARANTEED to use __lt__ when making comparaisons between two objects

"""

import unittest


class LargestNumberTest(unittest.TestCase):
    class Key(str):
        def __lt__(x, y):
            x_y = x + y
            y_x = y + x
            lt = x_y < y_x
            # print(x_y, y_x, lt)
            return lt

    def largestNumber(self, nums):
        # print(nums)
        nums = sorted(map(str, nums), key=self.Key, reverse=True)
        # print(nums)
        result = ''.join(nums)
        return '0' if result[:1] == '0' else result

    def test_basic(self):
        self.assertEqual(self.largestNumber([0, 0, 1]), "100")
        self.assertEqual(self.largestNumber([0, 0]), "0")
        self.assertEqual(self.largestNumber([10, 2]), "210")
        self.assertEqual(self.largestNumber([9, 3, 30, 34, 5]), "9534330")
        self.assertEqual(self.largestNumber([1440, 7548, 4240, 6616, 733, 4712, 883, 8, 9576]),
                         "9576888375487336616471242401440")
