"""
### Problem ###

https://leetcode.com/problems/random-flip-matrix/description/

You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are
initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns
the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try
to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

Note:

    1. 1 <= n_rows, n_cols <= 10000
    2. 0 <= row.id < n_rows and 0 <= col.id < n_cols
    3. flip will not be called when the matrix has no 0 values left.
    4. the total number of calls to flip and reset will not exceed 1000.

Example 1:

Input:
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]

Output: [null,[0,1],[1,2],[1,0],[1,1]]

Example 2:

Input:
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]

Output: [null,[0,0],[0,1],null,[0,0]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows
and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.

### Notes ###

My initial solution was to create an array of size row*col.  Each index of the array had index to the array reset to
value 0.

I hit Time Limit Exceeded.

Then, looked into Python API and found random.sample.  Solution below also hit Time Limit Exceeded.

I got hints from discussions and saw people using set.  I am not quite familiar with set, so decided to try to use
find an answer using that structure.

"""

import random
import unittest


class RandomFlipMatrix():
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_rows = n_rows
        self.n_cols = n_cols

        self.reset()

    def flip(self):
        """
        :rtype: List[int]
        """

        choices = self.n_rows * self.n_cols

        while True:
            i = random.randint(0, choices - 1)
            if i in self.matrix:
                continue
            else:
                self.matrix.add(i)
                index_to_flip = i
                break

        row = index_to_flip % self.n_rows
        col = int(index_to_flip / self.n_rows)

        return [row, col]

    def reset(self):
        """
        :rtype: void
        """
        self.matrix = set()


class RandomFlipMatrixTest(unittest.TestCase):
    def test_basic(self):
        m = RandomFlipMatrix(1, 1)

        for _ in range(1):
            result = m.flip()
            print("result", result)

    pass
