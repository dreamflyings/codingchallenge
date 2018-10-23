"""
https://leetcode.com/problems/walking-robot-simulation/description/

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot
can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units

Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid
square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from
the origin.

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)

Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

* 0 <= commands.length <= 10000
* 0 <= obstacles.length <= 10000
* -30000 <= obstacle[i][0] <= 30000
* -30000 <= obstacle[i][1] <= 30000
* The answer is guaranteed to be less than 2 ^ 31.

---

This was easy, but PITA.

"""


class Position:
    def __init__(self, obstacles):
        NORTH, SOUTH, EAST, WEST = (1, 2, 3, 4)  # HACK
        self.x = 0
        self.y = 0
        self.dir = NORTH
        self.obstacles = set(list(map(tuple, obstacles)))

    def turnLeft(self):
        NORTH, SOUTH, EAST, WEST = (1, 2, 3, 4)  # HACK
        if self.dir == NORTH:
            self.dir = WEST
        elif self.dir == SOUTH:
            self.dir = EAST
        elif self.dir == EAST:
            self.dir = NORTH
        elif self.dir == WEST:
            self.dir = SOUTH

    def turnRight(self):
        NORTH, SOUTH, EAST, WEST = (1, 2, 3, 4)  # HACK
        if self.dir == NORTH:
            self.dir = EAST
        elif self.dir == SOUTH:
            self.dir = WEST
        elif self.dir == EAST:
            self.dir = SOUTH
        elif self.dir == WEST:
            self.dir = NORTH

    def robotConfig(self):
        NORTH, SOUTH, EAST, WEST = (1, 2, 3, 4)  # HACK

        if self.dir == NORTH:
            return (lambda x: x, lambda y: y + 1)
        elif self.dir == SOUTH:
            return (lambda x: x, lambda y: y - 1)
        elif self.dir == EAST:
            return (lambda x: x + 1, lambda y: y)
        elif self.dir == WEST:
            return (lambda x: x - 1, lambda y: y)

    def moveRobot(self, steps):
        fx, fy = self.robotConfig()
        distance = 0
        i = 0
        while i < steps:
            nx = fx(self.x)
            ny = fy(self.y)
            if (nx, ny) not in self.obstacles:
                distance = max(distance, nx * nx + ny * ny)
                self.x = nx
                self.y = ny
                i += 1
            else:
                break

        return distance


class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        p = Position(obstacles)
        distance = 0

        for command in commands:
            if command == -1:
                # right 90 degrees
                p.turnRight()
            elif command == -2:
                # left 90 degrees
                p.turnLeft()
            elif command >= 1 and command <= 9:
                distance = max(distance, p.moveRobot(command))

        return distance
