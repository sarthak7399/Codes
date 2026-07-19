# https://leetcode.com/problems/cyclically-rotating-a-grid/

# Example 1:
# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)      # Number of rows
        n = len(grid[0])   # Number of columns

        # Number of concentric layers in the grid
        layers = min(m, n) // 2

        # Process each layer independently
        for layer in range(layers):

            nums = []  # Stores elements of current layer

            # Define boundaries of current layer
            top = layer
            bottom = m - layer - 1
            left = layer
            right = n - layer - 1

            # Extract top row
            for j in range(left, right + 1):
                nums.append(grid[top][j])

            # Extract right column (excluding corners)
            for i in range(top + 1, bottom):
                nums.append(grid[i][right])

            # Extract bottom row (right → left)
            for j in range(right, left - 1, -1):
                nums.append(grid[bottom][j])

            # Extract left column (bottom → top, excluding corners)
            for i in range(bottom - 1, top, -1):
                nums.append(grid[i][left])

            length = len(nums)

            # Effective rotation (avoid unnecessary full rotations)
            rotate = k % length

            # Rotate layer elements left by 'rotate' positions
            rotated = nums[rotate:] + nums[:rotate]

            idx = 0  # Pointer for rotated values

            # Write rotated values back to top row
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1

            # Write back to right column
            for i in range(top + 1, bottom):
                grid[i][right] = rotated[idx]
                idx += 1

            # Write back to bottom row
            for j in range(right, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            # Write back to left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid