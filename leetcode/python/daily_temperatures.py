"""
### Problem ###

https://leetcode.com/problems/daily-temperatures/description/

Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would
have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
[1, 1, 4, 2, 1, 1, 0, 0].

### Notes ###

This was a b**.  Had to resort to looking at (and studying!) the solution :(

Now have better grasp of how to properly use deque to implement a stack.  It is easy in theory, but proved to be
bug prone for me.

Basically the idea is to work backwards.

i temps[i] stack   |           | stack'
7 73       []      |             [7]      # empty stack, push
6 76       [7]     | 76 > head | [6]      # pop
6 76       [7]     | 76 > head | []       # pop, then push [6]
5 72       [6]     | 72 < head | [5 6]
4 69       [5 6]   | 69 < head | [4 5 6]
3 71       [4 5 6]  # 71 > 69, pop; 71 < 72 ; result =  5 - 3 = 2, push 3(71

[..]

"""

import collections
import unittest


class DailyTemperaturesTest(unittest.TestCase):

    def dailyTemperatures(self, temps):
        stack = collections.deque()
        days_until_warm = collections.deque()

        num_temps = len(temps)

        for i in reversed(range(0, num_temps)):
            if len(stack) == 0:
                stack.appendleft(i)
                days_until_warm.appendleft(0)
            else:
                found = False
                while len(stack) > 0:
                    it = temps[i]
                    ht = temps[stack[0]]
                    if ht > it:
                        found = True
                        break
                    else:
                        stack.popleft()

                if found:
                    days_until_warm.appendleft(stack[0] - i)
                    stack.appendleft(i)
                else:
                    stack.appendleft(i)
                    days_until_warm.appendleft(0)

        return list(days_until_warm)

    def test_basic(self):
        temps = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(expected, self.dailyTemperatures(temps))

    def test_corner(self):
        temps = [80, 34, 80, 80, 80, 34, 34, 34, 34, 34]
        expected = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, self.dailyTemperatures(temps))

    def test_corner_2(self):
        temps = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
        expected = [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]
        self.assertEqual(expected, self.dailyTemperatures(temps))
