"""
### Problem ###
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

### Notes ###


Examples:

([)]
push (
push [
pop -> ) != top

()[]{}
push (
pop -> )
push [
[..]

"""

import unittest


class ValidParenthesesTest(unittest.TestCase):
    def valid_parentheses(self, s):
        stack = []
        if s == "" or s is None:
            return True
        for p in list(s):
            if p == '(':
                stack.append(')')
            elif p == '[':
                stack.append(']')
            elif p == '{':
                stack.append('}')
            elif p == ')' or p == ']' or p == '}':
                if len(stack) < 1:
                    return False
                if stack.pop() != p:
                    return False
            else:
                return False

        return True if len(stack) == 0 else False

    def test_example_1(self):
        self.assertTrue(self.valid_parentheses("()"))

    def test_example_2(self):
        self.assertTrue(self.valid_parentheses("()[]{}"))

    def test_example_3(self):
        self.assertFalse(self.valid_parentheses("(]"))

    def test_example_4(self):
        self.assertFalse(self.valid_parentheses("([)]"))

    def test_example_5(self):
        self.assertTrue(self.valid_parentheses("{[]}"))

    def test_example_6(self):
        self.assertFalse(self.valid_parentheses("]"))
