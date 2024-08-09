# https://leetcode.com/problems/magic-squares-in-grid/

# Example 1:
# Input: grid = 
# [[4,3,8,4],
# [9,5,1,9],
# [2,7,6,2]]
# Output: 1
# Explanation: The following subgrid is a 3 x 3 magic square:
# [[4,3,8],
#  [9,5,1],
#  [2,7,6]] 
# as sum of its right diagonal elements: 4 + 5 + 6 = 15 
# and sum of its left diagonal elements: 3 + 5 + 7 = 15.

from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0 
        count = 0
        
        for i in range(m - 2):
            for j in range(n - 2):
                d = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        d.add(grid[k][l])
                
                if d == set(range(1, 10)):
                    if (grid[i][j] + grid[i][j+1] + grid[i][j+2] == 
                        grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] ==
                        grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] ==
                        grid[i][j] + grid[i+1][j] + grid[i+2][j] ==
                        grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] ==
                        grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] ==
                        grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] ==
                        grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]):
                        count += 1
                
        return count