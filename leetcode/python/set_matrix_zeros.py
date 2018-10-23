"""
### Problem ###

https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
https://leetcode.com/problems/set-matrix-zeroes/description/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

- A straight forward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?

### Notes ###

Constant space solution O(n).

1 hour later, no progress, and needed a hint.

Hints:

The difficulty is that we have to store some information about which zero is original and which zero is
created by us. We can store the information in the first row and first column of the origin matrix. So we need two
flags to record that does the first row and first column have original zero or not.

"""

import unittest


class SetMatrixZerosTest(unittest.TestCase):
    def set_zeros(self, m):
        num_rows = len(m)
        num_cols = len(m[0])

        # does the 1st row have any 0s?
        first_row_zero = False
        for c in range(num_cols):
            if m[0][c] == 0:
                first_row_zero = True
                break

        # does the 1st col have any 0s?
        first_col_zero = False
        for r in range(num_rows):
            if m[r][0] == 0:
                first_col_zero = True
                break

        # identify rows and cols that need to be cleared, do not look at top row or left col
        for r in range(1, num_rows):
            for c in range(1, num_cols):
                if m[r][c] == 0:
                    m[r][0] = 0  # need to clear row r, save state in left col
                    m[0][c] = 0  # need to clear col r, save state in top row

        # clear cols, except left most
        for r in range(1, num_rows):
            if m[r][0] == 0:
                for c in range(1, num_cols):
                    m[r][c] = 0

        # clear rows, except top most
        for c in range(1, num_cols):
            if m[0][c] == 0:
                for r in range(1, num_rows):
                    m[r][c] = 0

        # clear top most row, if applicable
        if first_row_zero:
            for c in range(num_cols):
                m[0][c] = 0

        # clear left most col, if applicable
        if first_col_zero:
            for r in range(num_rows):
                m[r][0] = 0

        return m

    def test_basic_1(self):
        input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

        output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.assertEqual(output, self.set_zeros(input))

    def test_basic_2(self):
        input = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        output = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.assertEqual(output, self.set_zeros(input))
