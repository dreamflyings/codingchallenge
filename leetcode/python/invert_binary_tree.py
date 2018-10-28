"""
https://leetcode.com/problems/invert-binary-tree/description/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:

This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you
can’t invert a binary tree on a whiteboard so f*** off.

### Notes ###

Traverse tree: 1 2 3 4 6 7 9

Reverse of traversed tree: 9 7 6 4 3 2 1

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None
        else:
            right = self.invertTree(root.left)
            left = self.invertTree(root.right)

            root.right = right
            root.left = left
            return root

