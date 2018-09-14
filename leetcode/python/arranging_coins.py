"""
### Problem ###
https://leetcode.com/problems/arranging-coins/description/

### Notes ###

I originally went for something WAY more complicated.  This is O(n).  Believe it would be possible to solve in O(log n)

loop end -> end-(i+1) >=0

start i  end cont?
5     1  4   4-2 >= 0, yes
4     2  2   2-3 < 0, no <-- 2


3     1 2  2-(2) >= 0, yes
2     2 0


start i end cont?
10    1 9
9     2 7
7     3 4   4-(4) >= 0, yes
4     4 0


"""


class ArrangingCoinsTest(object):
    def arrangeCoins(self, n):

        if n == 0:
            return 0

        if n == 1:
            return 1

        i = 1
        start = n

        while True:
            end = start - i
            if (end - i - 1) < 0: break

            start = end
            i += 1

        return i


"""
i = 0
while remain > i:
    remain -= i
    i += 1

return i-1
"""
