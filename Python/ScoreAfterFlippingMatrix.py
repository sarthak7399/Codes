# https://leetcode.com/problems/score-after-flipping-matrix/

# Example 1:
# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        num_rows, num_cols = len(grid), len(grid[0])
        
        # Initialize the result with the score of the first column
        score = (1 << (num_cols - 1)) * num_rows

        # Iterate through the columns starting from the second one
        for col_idx in range(1, num_cols):
            # Calculate the value of the current column
            col_val = 1 << (num_cols - 1 - col_idx)
            # Count the number of rows with the same value as the first element in the column
            same_count = 0
            
            # Iterate through the rows
            for row_idx in range(num_rows):
                if grid[row_idx][col_idx] == grid[row_idx][0]:
                    same_count += 1
            
            # Update the score based on the maximum count of same and different values in the column
            score += max(same_count, num_rows - same_count) * col_val

        return score
