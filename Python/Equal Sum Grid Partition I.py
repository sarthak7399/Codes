# https://leetcode.com/problems/equal-sum-grid-partition-i/

# Example 1:
# Input: grid = [[1,4],[2,3]]
# Output: true
# Explanation:
# A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

class Solution:
    def canPartitionGrid(self, grid):
        
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])

        # sumGrid[i][j] → sum of submatrix from (0,0) to (i,j)
        sumGrid = [[0] * n for _ in range(m)]

        # -------- Step 1: Build 2D prefix sum --------

        # First row (only horizontal accumulation)
        pref_sum = 0
        for j in range(n):
            pref_sum += grid[0][j]
            sumGrid[0][j] = pref_sum

        # Remaining rows
        for i in range(1, m):
            pref_sum = 0  # row-wise prefix sum
            for j in range(n):
                pref_sum += grid[i][j]

                # Add current row sum + sum from above row
                sumGrid[i][j] = pref_sum + sumGrid[i - 1][j]

        # Total sum of entire grid
        total_sum = sumGrid[m - 1][n - 1]

        # -------- Step 2: Try vertical cuts (column cuts) --------
        # Check if splitting between columns gives equal sum
        for j in range(n - 1):

            # Left part sum = sumGrid[m-1][j]
            # Right part sum = total_sum - left
            if sumGrid[m - 1][j] == total_sum - sumGrid[m - 1][j]:
                return True

        # -------- Step 3: Try horizontal cuts (row cuts) --------
        # Check if splitting between rows gives equal sum
        for i in range(m - 1):

            # Top part sum = sumGrid[i][n-1]
            # Bottom part sum = total_sum - top
            if sumGrid[i][n - 1] == total_sum - sumGrid[i][n - 1]:
                return True

        # If no valid partition found
        return False