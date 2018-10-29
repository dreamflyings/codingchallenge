"""
https://leetcode.com/problems/flatten-2d-vector/description/

### Notes ###

* Read the f*kng question!!!

Implement an iterator to flatten a 2d vector.

Example:

Input: 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]

Output: [1,2,3,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,2,3,4,5,6].
"""


class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.num_rows = len(vec2d)
        self.num_elems = 0
        for r in range(self.num_rows):
            self.num_elems += len(self.vec2d[r])
        self.remain_elems = self.num_elems

    def next(self):
        """
        :rtype: int
        """
        ans = -1
        for r in range(self.num_rows):
            if len(self.vec2d[r]) > 0:
                ans = self.vec2d[r][0]
                self.vec2d[r] = self.vec2d[r][1:]
                self.remain_elems -= 1
                break
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.remain_elems > 0


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
