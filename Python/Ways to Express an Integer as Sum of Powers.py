# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

# Example 1:
# Input: n = 10, x = 2
# Output: 1
# Explanation: We can express n as the following: n = 32 + 12 = 10.
# It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.

MOD = 1_000_000_007  # Large prime for modulo operations to avoid overflow

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # Step 1: Precompute all powers i^x that are <= n
        powers = []
        i = 1
        while True:
            p = pow(i, x)       # Compute i^x
            if p > n:           # Stop if power exceeds target sum
                break
            powers.append(p)    # Store valid power
            i += 1

        # Step 2: Initialize DP array
        # dp[s] = number of ways to make sum 's' using selected powers
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to make sum 0 (pick nothing)

        # Step 3: For each power, update dp array (classic subset sum logic)
        for p in powers:
            for s in range(n, p - 1, -1):  # Go backwards to avoid reusing the same number multiple times
                dp[s] = (dp[s] + dp[s - p]) % MOD

        # Step 4: The answer is number of ways to form sum n
        return dp[n]
