"""
### Problem ###

Check if a decimal integer is a palindrome.

### Notes ###

12345
       /10     %10
12345  1234    5
1234   123     4
123    12      3
12     1       2
1      0       1

12345 != 54321

32323

      /10    %10
32323 3232   3
3232  323    2
323   32     3
32    3      2
3     0      3

My solution is O(N) with space complexity O(N).

The solution in the book offers a solution with space complexity of O(1).

"""

import math
import unittest


class CheckIfIntegerIsPalindrome(unittest.TestCase):
    def check_palindrome(self, number):
        # corner cases
        if number < 0: return False
        if number == 0: return True

        result = []

        i = number

        while True:
            remain = i % 10
            i = int(i / 10)
            result.append(remain)
            if i == 0:
                break

        final = 0

        for i in range(len(result)):
            digit = result.pop()
            final += int(math.pow(10, i)) * digit

        return (number == final)

    def test_basic(self):
        self.assertEqual(False, self.check_palindrome(-1))
        self.assertEqual(True, self.check_palindrome(0))
        self.assertEqual(False, self.check_palindrome(12345))
        self.assertEqual(True, self.check_palindrome(32323))
