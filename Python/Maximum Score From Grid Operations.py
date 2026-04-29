# https://leetcode.com/problems/maximum-score-from-grid-operations/

# Example 1:
# Input: grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]
# Output: 11
# Explanation:
# In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is grid[3][0] + grid[1][2] + grid[3][3] which is equal to 11.

from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # If only one column, no transitions possible → score = 0
        if m == 1:
            return 0

        # Prefix sum for each column:
        # col[j][i] = sum of values from row 0 to i-1 in column j
        col = [[0] * (n + 1) for _ in range(m)]
        for j in range(m):
            for i in range(n):
                col[j][i + 1] = col[j][i] + grid[i][j]

        # dp[curr][prev]:
        # maximum score when current column uses split at 'curr'
        # and previous column used split at 'prev'
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Helper arrays to optimize transitions
        prefMax = [[0] * (n + 1) for _ in range(n + 1)]
        suffMax = [[0] * (n + 1) for _ in range(n + 1)]

        # Iterate over columns (starting from second column)
        for c in range(1, m):

            newdp = [[0] * (n + 1) for _ in range(n + 1)]

            # Try all possible splits for current and previous columns
            for curr in range(n + 1):
                for prev in range(n + 1):

                    if curr <= prev:
                        # Case 1: current split is above or equal to previous
                        # Gain comes from current column
                        gain = col[c][prev] - col[c][curr]

                        newdp[curr][prev] = max(
                            newdp[curr][prev],
                            suffMax[prev][0] + gain  # best from suffix
                        )
                    else:
                        # Case 2: current split is below previous
                        # Gain comes from previous column
                        gain = col[c - 1][curr] - col[c - 1][prev]

                        newdp[curr][prev] = max(
                            newdp[curr][prev],
                            suffMax[prev][curr],            # no gain case
                            prefMax[prev][curr] + gain      # gain from prefix
                        )

            # Build prefix and suffix maximums for optimization
            for curr in range(n + 1):

                # Prefix max initialization
                prefMax[curr][0] = newdp[curr][0]

                # Build prefix max (left → right)
                for prev in range(1, n + 1):
                    penalty = 0

                    # If prev > curr, subtract overlap penalty
                    if prev > curr:
                        penalty = col[c][prev] - col[c][curr]

                    prefMax[curr][prev] = max(
                        prefMax[curr][prev - 1],
                        newdp[curr][prev] - penalty
                    )

                # Suffix max initialization
                suffMax[curr][n] = newdp[curr][n]

                # Build suffix max (right → left)
                for prev in range(n - 1, -1, -1):
                    suffMax[curr][prev] = max(
                        suffMax[curr][prev + 1],
                        newdp[curr][prev]
                    )

            # Move to next column
            dp = newdp

        # Final answer:
        # We consider extreme splits (top = 0 or bottom = n)
        ans = 0
        for k in range(n + 1):
            ans = max(ans, dp[0][k], dp[n][k])

        return ans