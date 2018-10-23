# https://leetcode.com/problems/fizz-buzz/description/


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def f(x):
            retval = ""
            #print(x, x % 3, x % 5)
            if (x % 3) == 0:
                retval += "Fizz"
            if (x % 5) == 0:
                retval += "Buzz"
            if not retval:
                retval = str(x)
            return retval

        return [f(i) for i in range(1, n + 1)]
