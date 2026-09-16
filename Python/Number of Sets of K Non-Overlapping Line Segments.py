# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

# Example 1:
# Input: n = 4, k = 2
# Output: 5
# Explanation: The two line segments are shown in red and blue.
# The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.


import math

# Method 1 : DP
class Solution:
    def numberOfSets(self, n, k):
        # Modulo to keep the result within manageable limits.
        MOD = 10**9 + 7

        # dp[i][j] = number of ways to choose j segments
        # using points from 0 to i.
        dp = [[0] * (k + 1) for _ in range(n)]

        # There is exactly one way to choose 0 segments:
        # choose nothing.
        for i in range(n):
            dp[i][0] = 1

        # Build the DP for choosing 1 to k segments.
        for j in range(1, k + 1):
            # Stores the cumulative number of ways to form
            # j-1 segments before the current point.
            total = 0

            for i in range(1, n):
                # Add ways to form j-1 segments using points
                # before i. These can be extended by ending
                # a new segment at i.
                total = (total + dp[i - 1][j - 1]) % MOD

                # Two possibilities:
                # 1. Do not use point i as the end of a segment.
                # 2. End a segment at point i, represented by 'total'.
                dp[i][j] = (dp[i - 1][j] + total) % MOD

        # Return the number of ways to choose exactly k segments
        # using points from 0 to n-1.
        return dp[n - 1][k]


# Method 2 : Math Combinatorics
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # The number of ways to choose k non-overlapping segments
        # among n points can be represented using the combination:
        # C(n - 1 + k, 2 * k)
        #
        # Take the result modulo 1e9 + 7 as required.
        return math.comb(n - 1 + k, 2 * k) % int(1e9 + 7)