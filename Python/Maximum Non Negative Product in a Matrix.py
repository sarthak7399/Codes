# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

# Example 1:
# Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
# Output: -1
# Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

class Solution:
    def maxProductPath(self, grid):
        
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Modulo as required
        MOD = 10**9 + 7

        # mx[i][j] → maximum product to reach (i, j)
        # mn[i][j] → minimum product to reach (i, j)
        # (we track both because negative numbers can flip sign)
        mx = [[0] * n for _ in range(m)]
        mn = [[0] * n for _ in range(m)]

        # Base case: starting cell
        mx[0][0] = mn[0][0] = grid[0][0]

        # -------- First row --------
        # Only one way → move from left
        for j in range(1, n):
            mx[0][j] = mn[0][j] = mx[0][j - 1] * grid[0][j]

        # -------- First column --------
        # Only one way → move from top
        for i in range(1, m):
            mx[i][0] = mn[i][0] = mx[i - 1][0] * grid[i][0]

        # -------- Fill DP tables --------
        for i in range(1, m):
            for j in range(1, n):

                # Current cell value
                x = grid[i][j]

                # Possible products from top
                a = mx[i - 1][j] * x
                b = mn[i - 1][j] * x

                # Possible products from left
                c = mx[i][j - 1] * x
                d = mn[i][j - 1] * x

                # Maximum product at (i, j)
                mx[i][j] = max(a, b, c, d)

                # Minimum product at (i, j)
                mn[i][j] = min(a, b, c, d)

        # Final answer at bottom-right cell
        ans = mx[m - 1][n - 1]

        # If maximum product is negative → return -1
        # else return modulo value
        return -1 if ans < 0 else ans % MOD