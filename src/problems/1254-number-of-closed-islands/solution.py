import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import Dict, List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def color(row: int, col: int, color: int):
            to_visit = [(row, col)]
            visited = set()

            while len(to_visit) > 0:
                plot = to_visit.pop(0)

                p_row, p_col = plot[0], plot[1]

                if not plot in visited:
                    grid[p_row][p_col] = color

                    if p_row > 0 and grid[p_row - 1][p_col] == 0:
                        to_visit.append((p_row - 1, p_col))

                    if p_row < len(grid) - 1 and grid[p_row + 1][p_col] == 0:
                        to_visit.append((p_row + 1, p_col))

                    if p_col < len(grid[p_row]) - 1 and grid[p_row][p_col + 1] == 0:
                        to_visit.append((p_row, p_col + 1))
                    
                    if p_col > 0 and grid[p_row][p_col - 1] == 0:
                        to_visit.append((p_row, p_col - 1))

                    visited.add(plot)

        island_no = 0
        
        height = len(grid)
        width = len(grid[0])

        for col in range(width):
            if grid[0][col] == 0:
                color(0, col, 2)
            if grid[height - 1][col] == 0:
                color(height - 1, col, 2)

        for row in range(1, height - 1):
            if grid[row][0] == 0:
                color(row, 0, 2)
            if grid[row][width - 1] == 0:
                color(row, width - 1, 2)

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0:
                    island_no -= 1
                    color(row, col, island_no)

        return abs(island_no)

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_closedIsland(self):
        solution = Solution()

        self.assertEqual(
            solution.closedIsland(
                [[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[0,1,1,1,0]]
            ),
            1
        )

        self.assertEqual(
            solution.closedIsland(
                [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
            ),
            2
        )

        self.assertEqual(
            solution.closedIsland(
                [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
            ),
            1
        )

        self.assertEqual(
            solution.closedIsland([
                [1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1],
                [1,0,1,1,1,0,1],
                [1,0,1,0,1,0,1],
                [1,0,1,1,1,0,1],
                [1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1]
            ]),
            2
        )

if __name__ == '__main__':
    unittest.main()
