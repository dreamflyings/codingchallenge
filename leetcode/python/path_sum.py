"""
### Problem ###


https://leetcode.com/problems/path-sum/description/

      5
     / \
    4   8
   /   / \
  11  13  14
 /  \      \
7    2      11

root to leaf path, check sum

in order traveral


push 5         left not None
push 5,4       left not None
push 5,4,11    left not None
push 5,4,11,7  left is  None  visit
pop
push 5,4,11,2  left is  None  visit

"""

import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(unittest.TestCase):
  def traverse(self, node, s, path, found):
    path.append(node.val)

    if node.left is not None:
      self.traverse(node.left, s, path, found)

    if node.right is not None:
      self.traverse(node.right,s,  path, found)

    if node.left is None and node.left is None:
      #print(path)
      if sum(path) == s:
        found.append(True)

    path.pop()

  def hasPathSum(self, root, s):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """

    if root is None:
      return False

    path = []
    found = []

    self.traverse(root, s, path, found)

    return True if found != [] else False

  def test_simple(self):
    tree = {}

    for x in [5, 4, 8, 11, 13, 14, 7, 2, 1]:
        n = TreeNode(x)
        tree[x] = n

    tree[5].left = tree[4]
    tree[5].right = tree[8]

    tree[4].left = tree[11]

    tree[8].left = tree[13]
    tree[8].right = tree[4]

    tree[11].left = tree[7]
    tree[11].right = tree[2]

    tree[14].right = tree[1]

    root = tree[5]

    self.assertTrue(self.hasPathSum(root, 22))

  def test_null(self):
    self.assertFalse(self.hasPathSum(None, 1))

  def test_small(self):
    #[-2, null, -3]
    tree = {}
    tree[-2] = TreeNode(-2)
    tree[-3] = TreeNode(-3)

    tree[-2].right = tree[-3]

    root = tree[-2]

    self.assertFalse(self.hasPathSum(root, -2))


unittest.main(exit=False)

