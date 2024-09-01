# https://leetcode.com/problems/count-sub-islands/

# Example 1:
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)  # Number of rows in the grids
        cols = len(grid1[0])  # Number of columns in the grids

        def dfs(row: int, col: int):
            # If the current cell is out of bounds or already visited, return
            if row < 0 or row >= rows or col < 0 or col >= cols or grid2[row][col] == 0:
                return

            # Mark the current cell as visited by setting it to 0
            grid2[row][col] = 0

            # Explore the four possible directions (up, down, left, right)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row - 1, col)

        # Remove all parts of grid2 that are not sub-islands of grid1
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    dfs(row, col)  # Mark all connected cells as visited

        subIslandCount = 0  # Initialize count of sub-islands
        
        # Count all sub-islands in grid2
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    dfs(row, col)  # Mark all connected cells as visited
                    subIslandCount += 1  # Increment sub-island count

        return subIslandCount
