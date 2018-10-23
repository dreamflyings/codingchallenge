"""
https://leetcode.com/problems/pascals-triangle-ii/description/

Given a non-negative index k where k ≤ 33, return the kth index row of the
Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above
it.

Example:

Input: 3

Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?

---

gr(3)
  p = gr(2)
  row = range(3)

"""


class Solution:
    def get_row(self, row_index):
        """
        :type row_index: int
        :rtype: List[int]
        """
        if row_index == 0:
            return [1]
        elif row_index == 1:
            return [1, 1]
        else:
            prev = self.get_row(row_index - 1)
            num_cols = row_index + 1
            row = [None for _ in range(num_cols)]
            row[0] = prev[0]
            row[-1] = prev[-1]

            for i in range(1, num_cols - 1):
                row[i] = prev[i - 1] + prev[i]

            return row
