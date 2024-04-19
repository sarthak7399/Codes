# https://leetcode.com/problems/number-of-islands/

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)  # Get the number of rows in the grid
        n = len(grid[0])  # Get the number of columns in the grid

        def DFS(i, j):
            grid[i][j] = '0'  # Mark the current cell as visited

            # Explore adjacent cells in four directions: up, left, down, right
            if i > 0 and grid[i-1][j] == '1':  # Check if the cell above is '1'
                DFS(i-1, j)  # Recursively explore the cell above
            
            if j > 0 and grid[i][j-1] == '1':  # Check if the cell to the left is '1'
                DFS(i, j-1)  # Recursively explore the cell to the left

            if i < m - 1 and grid[i+1][j] == '1':  # Check if the cell below is '1'
                DFS(i+1, j)  # Recursively explore the cell below

            if j < n - 1 and grid[i][j+1] == '1':  # Check if the cell to the right is '1'
                DFS(i, j+1)  # Recursively explore the cell to the right

        num = 0  # Initialize the number of islands to 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0': continue  # Skip visited cells
                num += 1  # Increment the number of islands
                DFS(i, j)  # Explore the island starting from the current cell
        
        return num  # Return the total number of islands
