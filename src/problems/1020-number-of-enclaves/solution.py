import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import Dict, List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def color(row: int, col: int, color: int) -> int:
            to_visit = [(row, col)]
            visited = set()

            while len(to_visit) > 0:
                plot = to_visit.pop(0)

                p_row, p_col = plot[0], plot[1]

                if not plot in visited:
                    grid[p_row][p_col] = color

                    if p_row > 0 and grid[p_row - 1][p_col] == 1:
                        to_visit.append((p_row - 1, p_col))

                    if p_row < len(grid) - 1 and grid[p_row + 1][p_col] == 1:
                        to_visit.append((p_row + 1, p_col))

                    if p_col < len(grid[p_row]) - 1 and grid[p_row][p_col + 1] == 1:
                        to_visit.append((p_row, p_col + 1))
                    
                    if p_col > 0 and grid[p_row][p_col - 1] == 1:
                        to_visit.append((p_row, p_col - 1))

                    visited.add(plot)

            return len(visited)

        height = len(grid)
        width = len(grid[0])

        for col in range(width):
            if grid[0][col] == 1:
                color(0, col, -1)
            if grid[height - 1][col] == 1:
                color(height - 1, col, -1)

        for row in range(1, height - 1):
            if grid[row][0] == 1:
                color(row, 0, -1)
            if grid[row][width - 1] == 1:
                color(row, width - 1, -1)

        island_sq = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1:
                    island_sq += 1

        return island_sq

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_numEnclaves(self):
        solution = Solution()

        self.assertEqual(
            solution.numEnclaves(
                [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
            ),
            3
        )

        self.assertEqual(
            solution.numEnclaves(
                [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
            ),
            0
        )

if __name__ == '__main__':
    unittest.main()
