# https://leetcode.com/problems/maximum-path-score-in-a-grid/

# Example 1:
# Input: grid = [[0, 1],[2, 0]], k = 1
# Output: 2
# Explanation:​​​​​​​
# The optimal path is:
# Cell	grid[i][j]	Score	Total
# Score	Cost	Total
# Cost
# (0, 0)	0	0	0	0	0
# (1, 0)	2	2	2	1	1
# (1, 1)	0	0	2	0	1
# Thus, the maximum possible score is 2.

from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])  # Grid dimensions

        # dp[i][j][c] = maximum score to reach cell (i, j)
        # using exactly 'c' non-zero cells so far
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        # Starting point: (0,0) with 0 cost and score 0
        dp[0][0][0] = 0

        # Traverse all cells
        for i in range(m):
            for j in range(n):
                for c in range(k + 1):

                    # Skip unreachable states
                    if dp[i][j][c] == -1:
                        continue

                    # Move DOWN
                    if i + 1 < m:
                        val = grid[i + 1][j]

                        # Cost increases if cell value is non-zero
                        cost = 0 if val == 0 else 1
                        nc = c + cost  # New cost

                        # Check if cost constraint is satisfied
                        if nc <= k:
                            dp[i + 1][j][nc] = max(
                                dp[i + 1][j][nc],
                                dp[i][j][c] + val  # Add value to score
                            )

                    # Move RIGHT
                    if j + 1 < n:
                        val = grid[i][j + 1]

                        # Cost increases if cell value is non-zero
                        cost = 0 if val == 0 else 1
                        nc = c + cost  # New cost

                        # Check if cost constraint is satisfied
                        if nc <= k:
                            dp[i][j + 1][nc] = max(
                                dp[i][j + 1][nc],
                                dp[i][j][c] + val  # Add value to score
                            )

        # Find the best score at destination (m-1, n-1)
        # among all allowed costs ≤ k
        ans = -1
        for c in range(k + 1):
            ans = max(ans, dp[m - 1][n - 1][c])

        return ans  # Maximum achievable score