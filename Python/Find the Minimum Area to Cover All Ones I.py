# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

# Example 1:
# Input: grid = [[0,1,0],[1,0,1]]
# Output: 6
# Explanation:
# The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])      # m = number of rows, n = number of columns

        # Initialize boundaries for the rectangle that will enclose all 1s
        minRow, maxRow = m, -1              # minRow = topmost row with 1, maxRow = bottommost row with 1
        minCol, maxCol = n, -1              # minCol = leftmost col with 1, maxCol = rightmost col with 1

        # Traverse the grid to find the extreme positions of 1s
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Update min and max row indices
                    minRow = min(minRow, i)
                    maxRow = max(maxRow, i)
                    # Update min and max column indices
                    minCol = min(minCol, j)
                    maxCol = max(maxCol, j)

        # Compute the area of the rectangle enclosing all 1s
        # +1 is added because indices are inclusive
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)
