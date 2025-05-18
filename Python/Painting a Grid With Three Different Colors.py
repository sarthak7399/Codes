# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

# Example 1:
# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are shown in the image above.

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from itertools import product
        from collections import defaultdict

        MOD = 10**9 + 7

        # Step 1: Generate all valid column colorings of height m
        # A column is valid if no two adjacent cells (vertically) have the same color
        def is_valid(col):
            return all(col[i] != col[i + 1] for i in range(len(col) - 1))

        colors = [0, 1, 2]  # We use 3 colors: 0 = Red, 1 = Green, 2 = Blue
        valid_cols = []
        for col in product(colors, repeat=m):
            if is_valid(col):
                valid_cols.append(col)  # Save only valid columns

        # Step 2: Build a compatibility map
        # compatible[c1] contains all columns c2 that can be adjacent to c1
        # i.e., no two corresponding cells in c1 and c2 are the same (horizontal rule)
        compatible = {}
        for c1 in valid_cols:
            compatible[c1] = []
            for c2 in valid_cols:
                if all(a != b for a, b in zip(c1, c2)):
                    compatible[c1].append(c2)

        # Step 3: Initialize the DP table
        # dp[col] = number of ways to color the grid ending with column `col`
        # For the first column, we can use any valid column once
        dp = defaultdict(int)
        for col in valid_cols:
            dp[col] = 1

        # Step 4: Fill DP table for each column from left to right (n columns total)
        for _ in range(1, n):
            new_dp = defaultdict(int)
            for col in valid_cols:
                # For current column `col`, sum all possible ways that it can follow a compatible previous column
                for prev in compatible[col]:
                    new_dp[col] = (new_dp[col] + dp[prev]) % MOD
            dp = new_dp  # Move to next column

        # Step 5: Return the total number of valid colorings for the full grid
        return sum(dp.values()) % MOD
