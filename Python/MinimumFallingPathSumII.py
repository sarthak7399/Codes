# https://leetcode.com/problems/minimum-falling-path-sum-ii/

# Example 1:
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation: 
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.

from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Get the number of rows in the grid
        num_rows = len(grid)
        
        # Initialize the dynamic programming array with the first row of the grid
        dp = grid[0]

        # Iterate through the remaining rows of the grid
        for i in range(1, num_rows):
            # Find the indices of the minimum and second minimum elements in the current row of the DP array
            min_index = dp.index(min(dp))
            second_min_index = dp.index(min(dp[:min_index] + dp[min_index + 1:]))
            
            # Update each element in the current row of the grid
            for j in range(num_rows):
                if j != min_index:
                    grid[i][j] += dp[min_index]
                else:
                    grid[i][j] += dp[second_min_index]
            
            # Update the DP array with the current row of the grid
            dp = grid[i]

        # Return the minimum falling path sum from the last row of the grid
        return min(dp)
