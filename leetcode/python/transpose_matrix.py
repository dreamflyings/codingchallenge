"""
https://leetcode.com/problems/transpose-matrix/description/

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.


Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Note:
1 <= A.length <= 1000
1 <= A[0].length <= 1000

---

num_rows = len(A)
num_cols = len(A[0])

transposed_num_rows = num_cols
transposed_num_cols = num_rows

---

Example 2:

num_rows = 2
num_cols = 3
t_num_rows = 3
t_num_cols = 2

1 2 3  1 4
4 5 6  2 5
       3 5

for r in [0, 1, 2]:
    row = [None, None, None]
    for c in [0, 1]:
        row[c] = A[c][r]
    rows.append(row)

Assume row = 1,

row[1][0] = A[0][1] = 2

"""


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        num_rows = len(A)
        num_cols = len(A[0])
        transposed_num_rows = num_cols
        transposed_num_cols = num_rows

        T = []
        for r in range(transposed_num_rows):
            row = [None for _ in range(transposed_num_cols)]
            for c in range(transposed_num_cols):
                row[c] = A[c][r]
            T.append(row)
        return T
