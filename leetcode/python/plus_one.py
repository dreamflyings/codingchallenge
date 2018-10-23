# Problem: https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [0] + digits

        num_digits = len(digits)

        carry = 0
        first = 1

        for i in reversed(range(num_digits)):
            sum = digits[i] + first + carry
            first = 0

            if sum > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = sum
                carry = 0

        while digits[0] == 0:
            digits = digits[1:]

        return digits
