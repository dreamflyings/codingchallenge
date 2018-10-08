# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
