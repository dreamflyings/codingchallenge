"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1 2 11
5.     11 12 21
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"


cas(5) 111221
 cas(4) -> 1211
  cas(3) 11 -> 21
   cas(2) # 1 -> 11
    cas(1) # 1
"""

class Solution:
    def countAndSay(self, n, say=""):
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            m = self.countAndSay(n-1)

            len_m = len(m)
            count = 1
            last = 0
            say = ""
            for i in range(1, len_m):
                curr = m[i]
                prev = m[i-1]
                last = i == len_m-1

                if last:
                    if curr == prev:
                        count += 1
                        say += "{}{}".format(count, prev)
                    else:
                        say += "{}{}1{}".format(count,prev, curr)
                else:
                    if curr == prev:
                        count += 1
                    else:
                        say += "{}{}".format(count, prev)
                        count = 1

            return say

