"""
### Problem ###

https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""

import random
import unittest

class RandomizedSet:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.set = set() 

  def insert(self, val):
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    if val in self.set:
        return False
    self.set.add(val)
    return True

  def remove(self, val):
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: int
    :rtype: bool
    """
    if val not in self.set:
        return False
    self.set.remove(val)
    return True

  def get_random(self):
    """
    Get a random element from the set.
    :rtype: int
    """
    return random.sample(self.set,1)[0]

