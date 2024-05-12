# https://leetcode.com/problems/largest-local-values-in-a-matrix/

# Example 1:
# Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]
# Explanation: The diagram above shows the original matrix and the generated matrix.
# Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)  # Assuming the grid is square for simplicity
        result = []
        
        # Iterate through the grid, excluding the outer border
        for i in range(1, n-1):
            new_grid_row = []
            for j in range(1, n-1):
                # Extract the 3x3 subgrid and find its max value
                max_val = max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1], grid[i][j], grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                )
                new_grid_row.append(max_val)
            result.append(new_grid_row)
        return result
