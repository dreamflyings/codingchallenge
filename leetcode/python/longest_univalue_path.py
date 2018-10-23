"""
https://leetcode.com/problems/longest-univalue-path/description/

Given a binary tree, find the length of the longest path where each node in the
path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of
edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:
2

f(1.1, 5)
  l = f(2.1, 5)
    l = f(3.1, 4) = 0
      1 != 1
    r = f(3.1, 4) = 0
      1 != 1
    4 != 4
  r = f(2.2, 5) = 2
    r = f(3.2, 5) = 2
      5==5

              5
             / \
            4   5
           / \   \
          1   1   5

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5

Output:
2

---

I had to resort to a solution to solve this. I first attempted inorder tree
search recording the value as we visit. This had corner cases.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathLength(self, root, value):
        if not root: return 0

        left = self.pathLength(root.left, root.val)
        right = self.pathLength(root.right, root.val)
        self.len = max(self.len, left + right)
        if value == root.val:
            return max(left, right) + 1
        return 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.len = 0
        self.pathLength(root, root.val)
        return self.len
