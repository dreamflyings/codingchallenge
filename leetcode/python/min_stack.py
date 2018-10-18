"""
https://leetcode.com/problems/min-stack/description/

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x)   -- Push element x onto stack.
pop()    -- Removes the element on top of the stack.
top()    -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
  MinStack minStack = new MinStack();

  minStack.push(-2);
  minStack.push(0);
  minStack.push(-3);
  minStack.getMin();   --> Returns -3.
  minStack.pop();
  minStack.top();      --> Returns 0.
  minStack.getMin();   --> Returns -2.

---

-2
-2 0
-2 0 -3
-2 0 <- 0 is top

"""
import sys

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

        n = len(self.min_stack)
        if n == 0:
            self.min_stack.append(x)
        elif x <= self.min_stack[n-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        size = len(self.stack)
        pop = self.stack[size-1]
        self.stack = self.stack[0:size-1]

        n = len(self.min_stack)
        if pop == self.min_stack[n-1]:
            self.min_stack = self.min_stack[0:n-1]

    def top(self):
        """
        :rtype: int
        """
        n = len(self.stack)
        return self.stack[n-1]

    def getMin(self):
        """
        :rtype: int
        """
        n = len(self.min_stack)
        return self.min_stack[n-1]

