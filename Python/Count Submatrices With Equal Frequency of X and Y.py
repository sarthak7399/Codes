# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

# Example 1:
# Input: grid = [["X","Y","."],["Y",".","."]]
# Output: 3

class Solution:
    def numberOfSubmatrices(self, grid):
        
        # Dimensions of grid
        n = len(grid)
        m = len(grid[0])

        # sum_mat[i][j] → stores prefix sum of values from (0,0) to (i,j)
        # where:
        #   'X' = +1
        #   'Y' = -1
        #   others = 0
        sum_mat = [[0]*m for _ in range(n)]

        # cntX[i][j] → counts number of 'X' from (0,0) to (i,j)
        cntX = [[0]*m for _ in range(n)]

        # Final result
        res = 0

        # Traverse the grid
        for i in range(n):
            for j in range(m):

                # Initialize current cell contribution
                val = 0   # contribution to sum_mat
                x = 0     # contribution to cntX

                # Assign values based on character
                if grid[i][j] == 'X':
                    val = 1
                    x = 1
                elif grid[i][j] == 'Y':
                    val = -1

                # Set initial values
                sum_mat[i][j] = val
                cntX[i][j] = x

                # Add value from top cell (prefix sum vertically)
                if i > 0:
                    sum_mat[i][j] += sum_mat[i-1][j]
                    cntX[i][j] += cntX[i-1][j]

                # Add value from left cell (prefix sum horizontally)
                if j > 0:
                    sum_mat[i][j] += sum_mat[i][j-1]
                    cntX[i][j] += cntX[i][j-1]

                # Subtract overlap (top-left cell) to avoid double counting
                if i > 0 and j > 0:
                    sum_mat[i][j] -= sum_mat[i-1][j-1]
                    cntX[i][j] -= cntX[i-1][j-1]

                # Check condition:
                # sum == 0 → equal number of X and Y
                # cntX > 0 → at least one X exists
                if sum_mat[i][j] == 0 and cntX[i][j] > 0:
                    res += 1

        return res