"""
https://leetcode.com/problems/backspace-string-compare/description/

Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

* 1 <= S.length <= 200
* 1 <= T.length <= 200
* S and T only contain lowercase letters and '#' characters.

Follow up:

Can you solve it in O(N) time and O(1) space?

---

This was "easy" but complicated. I would have easily got to the solution with
the help of an editor. Without, I would have struggled.

I refered to hit/solution to find a more-straightforward way to solve the
problem.

"""


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def f(s):
            skip = 0
            for x in reversed(s):
                if x == '#':
                    skip += 1
                elif skip:
                    # this acts like a state machine
                    skip -= 1
                else:
                    yield x

        # not O(1) space
        return list(f(list(S))) == list(f(list(T)))
