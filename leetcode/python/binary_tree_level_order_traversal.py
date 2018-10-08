# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None: return []

        q = [[root]]

        for level in q:
            tmp = []
            for n in level:
                if n.left: tmp.append(n.left)
                if n.right: tmp.append(n.right)
            if tmp: q.append(tmp)

        return [[x.val for x in level] for level in q]
