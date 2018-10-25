"""
https://leetcode.com/problems/moving-average-from-data-stream/description/

Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);

m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""


class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.q = []  # FIFO

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        if len(self.q) > self.size:
            self.q = self.q[1:]

        s = 0
        for x in self.q:
            s += x

        return s / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
