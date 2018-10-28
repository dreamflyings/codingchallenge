"""
https://leetcode.com/problems/diameter-of-binary-tree/description/

Given a binary tree, you need to compute the length of the diameter of the
tree. The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.

Example:

Given a binary tree
          1
         / \
        2   3
       / \
      4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of
edges between them.


### Notes ###

* Return longest path between two nodes of a tree

* This would be similar to the max depth of the binary tree, try to solve first...

* Calculating the depth of a binary tree was easy....... but does not consider diameter

* diameter is depth of left + depth of right + 1, max diameter = max(node diameter, max dia)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max_diameter = 1

        def depth_of_bin_tree(node):
            if not node: return 0
            else:
                l = depth_of_bin_tree(node.left)
                r = depth_of_bin_tree(node.right)
                self.max_diameter = max(self.max_diameter, l + r + 1)
                depth = max(l, r) + 1
                return depth

        depth_of_bin_tree(root)

        return self.max_diameter - 1
