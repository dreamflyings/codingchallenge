"""
### Problem ###

https://leetcode.com/problems/robot-return-to-origin/description/

There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

### Notes ###

Straightforward?


"""

import unittest


class RobotReturnToOriginTest(unittest.TestCase):
    def judgeCircle(self, moves):
        x = 0
        y = 0

        for move in list(moves):
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            elif move == "R":
                x += 1

        return True if (x == 0 and y == 0) else False

    def test_smoke(self):
        self.assertEqual(True, self.judgeCircle("UD"))
        self.assertEqual(False, self.judgeCircle("LL"))
