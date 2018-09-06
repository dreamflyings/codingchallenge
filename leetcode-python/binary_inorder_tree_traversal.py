"""
### Problem ###

https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1, null, 2, 3]
     1
   /   \
null     2
       /
      3

Output: [1, 3, 2]


Input: arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

                 0
           1         2
       3       4  5     6
   7      8  9


Follow up: Recursive solution is trivial, could you do it iteratively?

### Notes ###

https://leetcode.com/faq/#binary-tree

"""

import math
import unittest


class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BinaryInorderTreeTraversalTest(unittest.TestCase):
    def makeTree(self, levelOrderTree):
        if levelOrderTree == []:
            return None

        nodes = [ None if value is None else TreeNode(value) for value in levelOrderTree ]
 
        kids = nodes[::-1]

        root = kids.pop()

        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def inorderTraversal(self, root):
        """
        :type :root: TreeNode
        :rtype: List[int]
        """
        return [1, 3, 4]

    def test_basic(self):
        inputs = [[1, None, 2, 3]]

        for input in inputs:
            self.inorderTraversal(self.makeTree(input))

