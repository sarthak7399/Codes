# https://leetcode.com/problems/twisted-mirror-path-count/

# Example 1:
# Input: grid = [[0,1,0],[0,0,1],[1,0,0]]
# Output: 5
# Explanation:
# Number	Full Path
# 1	(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
# 2	(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
# 3	(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
# 4	(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
# 5	(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
# [M] indicates the robot attempted to enter a mirror cell and instead reflected.

from typing import List

# Transition matrices for each cell type (0 or 1).
# Each matrix defines how the number of paths from the left and top
# contributes to the updated path counts.

mat = [[[1, 1], [1, 1]], [[0, 1], [1, 0]]]

# Modulo value to prevent numbers from growing too large.
MOD = 10**9 + 7

class Solution:
    def uniquePaths(self, A: List[List[int]]) -> int:
        # Get the number of columns.
        n, left = len(A[0]), 0

        # dp[j] stores the number of paths reaching the current column from above.
        dp = [0] * n

        # Initialise the starting position with one path.
        dp[0] = 1

        # Process the grid row by row.
        for row in A:
            # Reset the left contribution at the beginning of each row.
            left = 0

            for j, c in enumerate(row):
                # Store the number of paths coming from the top before updating dp[j].
                top = dp[j]

                # Update the paths coming from the top using the cell's transition matrix.
                dp[j] = (left * mat[c][1][0] + top * mat[c][1][1]) % MOD

                # Update the paths coming from the left using the cell's transition matrix.
                left = (left * mat[c][0][0] + top * mat[c][0][1]) % MOD

        # Return the final path count.
        return left