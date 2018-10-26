"""
https://leetcode.com/problems/zigzag-iterator/description/

Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6]

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,3,2,4,5,6].

---

This one appears to be straightforward.

Mantain two pointers. Use yield. But there are corner cases.

Example 1:

[1, 2]
[3, 4, 5, 6]

w i1 i2 | w' i1' i2'
0  0. 0   1  1   0
1  1  0.  0  1   1
0  1. 1   1  2   1
1  2  1.  1  2   2
1  2  2.  1  2   3
1  2  3.  1  2   4

Example 2:
[]
[1]

w i1 i2 | w' i1' i2'



"""


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

        self.v1 = v1
        self.v2 = v2

        self.l1 = len(v1)
        self.l2 = len(v2)

        self.i1 = 0  # index into l1
        self.i2 = 0  # index into l2

        if self.l1 > 0:
            self.which = 0
        elif self.l2 > 0:
            self.which = 1

        self.count = 0

    def next(self):
        """
        :rtype: int
        """
        if self.which == 0:

            if self.i1 < self.l1:
                r = self.v1[self.i1]
                self.i1 += 1

            if self.i2 < self.l2:
                self.which = 1

            self.count += 1
            return r
        else:
            if self.i2 < self.l2:
                r = self.v2[self.i2]
                self.i2 += 1

            if self.i1 < self.l1:
                self.which = 0

            self.count += 1
            return r

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.v1 and not self.v2:
            return False

        return self.count < (self.l1 + self.l2)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
