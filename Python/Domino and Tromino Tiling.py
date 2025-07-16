# https://leetcode.com/problems/domino-and-tromino-tiling/

# Example 1:
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7  # To prevent integer overflow and ensure the result stays within bounds

        # Base cases:
        if n <= 1:
            return 1  # Only 1 way to tile a 1x1 board
        if n == 2:
            return 2  # Two ways: two vertical dominoes or two horizontal dominoes
        if n == 3:
            return 5  # Five configurations for a 1x3 board using dominoes and trominoes

        # dp[i] represents the number of ways to tile a 2 x i board
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 5

        # Fill the dp array using the recurrence relation:
        # dp[i] = 2 * dp[i-1] + dp[i-3]
        # The recurrence comes from:
        # - Adding a vertical domino to all (i-1) tilings
        # - Adding two horizontal dominoes to all (i-2) tilings (accounted in 2 * dp[i-1])
        # - Adding trominoes that affect 3 columns, hence dp[i-3]
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]
