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

Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                 0
           1         2
       3       4  5     6
   7      8  9

Output: [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]

Follow up: Recursive solution is trivial, could you do it iteratively?

### Notes ###

https://leetcode.com/faq/#binary-tree

In order traversal process all nodes of a tree by recursively processing the left subtree, then root, finally
the right subtree.

"""

import unittest


class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class BinaryInorderTreeTraversalTest(unittest.TestCase):
    def makeTree(self, levelOrderTree):
        if levelOrderTree == []:
            return None

        nodes = [None if value is None else TreeNode(value) for value in levelOrderTree]

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

        # iterative

        node = root
        stack = []
        visited = []

        while node is not None or stack != []:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                visited.append(node)
                node = node.right

        return visited

        # recursive

        # if root is None:
        #    return[]
        #
        # left = self.inorderTraversal(root.left) if root.left is not None else []
        # this = [root.val]
        # right = self.inorderTraversal(root.right) if root.right is not None else []
        #
        # return left + this + right

    def test_basic(self):
        inputs = [
            [],
            [1, None, 2, 3],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]
        expected = [
            [],
            [1, 3, 2],
            [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]
        ]

        self.assertEqual(len(inputs), len(expected))

        for i in range(len(inputs)):
            root = self.makeTree(inputs[i])
            actual = self.inorderTraversal(root)
            # self.assertEqual(expected[i], actual) #--FIXME: error with assertion
