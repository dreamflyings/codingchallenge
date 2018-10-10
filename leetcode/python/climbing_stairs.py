# https://leetcode.com/problems/climbing-stairs/description/
class Solution:

    def climbStairs(self, n, cache = {}):
        """
        :type n: int
        :rtype: int
        """
        ways_to_climb = 0

        if n in cache:
            ways_to_climb = cache[n]
        elif n == 0:
            ways_to_climb = 0
        elif n == 1:
            ways_to_climb = 1
        elif n == 2:
            ways_to_climb = 2
        else:
            ways_to_climb = self.climbStairs(n-1, cache) + self.climbStairs(n-2, cache)

        if n not in cache: cache[n] = ways_to_climb

        return ways_to_climb

