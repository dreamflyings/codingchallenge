"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

Given a string S of '(' and ')' parentheses, we add the minimum number of
parentheses ( '(' or ')', and in any positions ) so that the resulting
parentheses string is valid.

Formally, a parentheses string is valid if and only if:

* It is the empty string, or
* It can be written as AB (A concatenated with B), where A and B are valid
  strings, or
* It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must
add to make the resulting string valid.

Example 1:

Input: "())"
Output: 1

Example 2:

Input: "((("
Output: 3

Example 3:

Input: "()"
Output: 0

Example 4:

Input: "()))(("
Output: 4

Note:

* S.length <= 1000
* S only consists of '(' and ')' characters.

### Notes ###

* LIFO, use stack
* Iterate through parentheses, push/pop, return stack size?
* No, not that simple: ()))((
* If len(stack) == 0 and s == ')' then inc. count?

* )) => 2
* (( => 2
* )()
* ())

"""


class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        count = 0
        for s in S:
            if s == '(':
                stack.append('(')
            elif s == ')' and len(stack) == 0:
                count += 1
            elif s == ')' and stack[0] == '(':
                stack = stack[1:]

        return len(stack) + count
