# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

# Example 1:
# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
# Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

from typing import List
class Solution:
    def __init__(self):
        # Directions for moving up, right, down, left (used for DFS traversal)
        self.d = [0, 1, 0, -1, 0]  
        # Initialize starting row (r) and column (c)
        self.r = 0
        self.c = 0

    def DFS(self, i, j, grid):
        # Start DFS from the current cell (i, j)
        fish = grid[i][j]  # Initialize fish count with the number at the current cell
        grid[i][j] = 0  # Mark the cell as visited (set to 0)
        
        # Explore all 4 possible directions (up, right, down, left)
        for a in range(4):
            row = i + self.d[a]  # Calculate the new row based on the direction
            col = j + self.d[a + 1]  # Calculate the new column based on the direction
            
            # Check if the new position is out of bounds or a cell with no fish (0)
            if row < 0 or row >= self.r or col < 0 or col >= self.c or grid[row][col] == 0:
                continue  # Skip to the next direction if the move is invalid
            
            # Recursively call DFS to explore the neighboring cell and add the fish count
            fish += self.DFS(row, col, grid)
        
        # Return the total fish count found in this connected component
        return fish

    def findMaxFish(self, grid: List[List[int]]) -> int:
        # Set the number of rows (r) and columns (c) in the grid
        self.r = len(grid)
        self.c = len(grid[0])
        
        # Variable to store the maximum fish count found
        ans = 0
        
        # Traverse each cell in the grid
        for i in range(self.r):
            for j in range(self.c):
                # If the current cell has fish (greater than 0), start DFS
                if grid[i][j] > 0:
                    # Update the maximum fish count with the result from DFS
                    ans = max(ans, self.DFS(i, j, grid))

        # Return the maximum number of fish found in a connected component
        return ans
