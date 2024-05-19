# https://leetcode.com/problems/island-perimeter

# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0  # Initialize the perimeter counter
        rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
        
        for r in range(rows):  # Loop through each row
            for c in range(cols):  # Loop through each column
                if grid[r][c] == 1:  # Check if the current cell is land
                    perimeter += 4  # Increment the perimeter by 4 for each land cell
                    if r > 0 and grid[r-1][c] == 1:  # Check if the cell above is also land
                        perimeter -= 2  # Decrement the perimeter by 2 if adjacent land cells are found vertically
                    if c > 0 and grid[r][c-1] == 1:  # Check if the cell to the left is also land
                        perimeter -= 2  # Decrement the perimeter by 2 if adjacent land cells are found horizontally
        
        return perimeter  # Return the final perimeter count
