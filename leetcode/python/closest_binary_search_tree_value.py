"""
https://leetcode.com/problems/closest-binary-search-tree-value/description/

Given a non-empty binary search tree and a target value, find the value in the
BST that is closest to the target.

Note:

* Given target value is a floating point.
* You are guaranteed to have only one unique value in the BST that is closest
  to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        # why to only check 1 subtree? because that subtree is guaranteed to be closer to the target than the other subtree
        a = root.val
        child = root.left if target < a else root.right
        if not child: return a
        b = self.closestValue(child, target)
        return min((b, a), key=lambda x: abs(target - x))
