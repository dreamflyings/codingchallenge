"""
### Problem ###
https://leetcode.com/problems/string-to-integer-atoi/description/

### Notes ###
This one was easy, but a real pain in the behind.
"""

import math
import unittest


class StringToIntegerTest(unittest.TestCase):
    def atoi(self, str):
        str = str.lstrip(" ")

        if len(str) == 0: return 0

        starts_with_digit = str[0].isdigit()
        starts_with_negative = str[0] == "-"
        starts_with_positive = str[0] == "+"

        if not starts_with_digit and not starts_with_negative and not starts_with_positive:
            return 0

        if starts_with_positive:
            str = str[1:]

        if starts_with_negative:
            str = str[1:]

        found_digit = False
        delete_char = False

        l = []

        for char in str:
            is_digit = char.isdigit()

            case = [is_digit, found_digit, delete_char]

            if case == [0, 0, 0]:
                # "aa0"
                return 0
            elif case == [0, 1, 0]:
                delete_char = True  # start deleting characters
            elif case == [1, 0, 0]:
                found_digit = True
                l.append(char)
            elif case == [1, 1, 0]:
                # continue digit
                l.append(char)
            else:
                # skip digit
                pass

        i = 0
        result = 0
        while l:
            x = l.pop()
            result += int(x) * int(math.pow(10, i))
            i += 1

        maxint = int(math.pow(2, 31))

        result = -result if starts_with_negative else result

        if abs(result) >= abs(maxint):
            if result > 0:
                result = maxint - 1
            else:
                result = -maxint

        return result

    def test_plus_minus(self):
        self.assertEqual(0, self.atoi("+-2"))

    def test_minus_plus(self):
        self.assertEqual(0, self.atoi("-+2"))

    def test_plus(self):
        self.assertEqual(1, self.atoi("+1"))

    def test_float(self):
        self.assertEqual(3, self.atoi("3.14159"))

    def test_basic(self):
        self.assertEqual(42, self.atoi("42"))

    def test_whitespace_negative(self):
        self.assertEqual(-42, self.atoi("    -42"))

    def test_with_words(self):
        self.assertEqual(4193, self.atoi("4193 with words"))

    def test_invalid(self):
        self.assertEqual(0, self.atoi("words and 987"))

    def test_null(self):
        self.assertEqual(0, self.atoi(""))

    def test_bounds(self):
        self.assertEqual(-2147483648, self.atoi("-91283472332"))

    def test_hex(self):
        self.assertEqual(-12, self.atoi("-0012a42"))

    def test_corner(self):
        self.assertEqual(0, self.atoi("  +0 123"))

    def test_bounds_2(self):
        self.assertEqual(2147483647, self.atoi("2147483648"))
