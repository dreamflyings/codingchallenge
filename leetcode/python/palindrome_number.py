"""
https://leetcode.com/problems/palindrome-number/description/

Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false

Example 3:

Input: 10
Output: false

Follow up:

Could you solve it without converting the integer to a string?

    div10 mod10 | stack

121 12 1 | 1
12  1  2 | 1 2
1   0  1 | 1 2 1


10  1     0     | 0
1   0     1     | 0 1

1234 123 4
123  12  3
12   1   2
1    0   1 | 1 2 3 4

"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x_orig = x

        if x < 0:
            return False

        q = []
        div10 = None
        while div10 != 0:
            div10 = int(x / 10)
            mod10 = x % 10
            q.append(mod10)
            x = div10

        sum = 0
        l = len(q)
        print(q)
        for i in range(l):
            x = q[-1]
            sum += x * int(math.pow(10, i))
            q = q[:-1]

        return sum == x_orig
