"""
### Problem ###
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

### Notes ###

This was not immediately obvious and I had to resort to looking at hints.

For each point in the grid perform a depth first search starting at coordinate row, col.

Mark every point visited.

Stop the search (return 0) if you hit water.

If the search is complete, you have an island.

"""

from inspect import cleandoc
import unittest


class NumberOfIslandsTest(unittest.TestCase):
    def num_islands(self, grid):
        if grid == []: return 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        visited = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        def is_on_grid(row, col):
            x = False if (row < 0 or row >= num_rows or col < 0 or
                          col >= num_cols) else True
            return x

        def is_water(row, col):
            return True if grid[row][col] == "0" else False

        def is_land(row, col):
            x = True if (grid[row][col] == "1") else False
            return x

        def is_visited(row, col):
            if is_on_grid(row, col):
                x = visited[row][col]
            else:
                x = False
            return x

        def visit(row, col):
            assert is_visited(row, col) == 0
            visited[row][col] = 1

        def north(row, col):
            return (row - 1, col)

        def south(row, col):
            return (row + 1, col)

        def east(row, col):
            return (row, col + 1)

        def west(row, col):
            return (row, col - 1)

        def dfs(row, col):
            if not (is_on_grid(row, col) and
                    (is_visited(row, col) == 0) and is_land(row, col)):
                return 0
            visit(row, col)
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            return 1

        islands = 0

        for col in range(num_cols):
            for row in range(num_rows):
                islands += dfs(row, col)

        return islands

    def test_example_1(self):
        grid = cleandoc("""
        11110
        11010
        11000
        00000
        """).split('\n')

        input = list(map(lambda x: list(x), grid))
        self.assertEqual(1, self.num_islands(input))

    def test_example_2(self):
        grid = cleandoc("""
        11000
        11000
        00100
        00011
        """).split('\n')

        input = list(map(lambda x: list(x), grid))
        self.assertEqual(3, self.num_islands(input))

    def test_example_3(self):
        grid = cleandoc("""
        1011011
        """).split('\n')
        input = list(map(lambda x: list(x), grid))
        self.assertEqual(3, self.num_islands(input))

    def test_bounds_1(self):
        self.assertEqual(0, self.num_islands([]))
