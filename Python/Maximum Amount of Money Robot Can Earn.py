# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

# Example 1:
# Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
# Output: 8
# Explanation:
# An optimal path for maximum coins is:
# Start at (0, 0) with 0 coins (total coins = 0).
# Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
# Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
# Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
# Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).

from math import inf
from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        
        # Number of columns
        n = len(coins[0])
        
        # dp[j][k]:
        # j → column index (1-based for convenience)
        # k → number of "skips/neutralizations" used (0, 1, 2)
        # Value = maximum sum achievable till this position
        
        # Initialize DP with very small values
        dp = [[-inf] * 3 for _ in range(n + 1)]
        
        # Base case:
        # Before starting, at column 1 we can have 0 sum with any k
        dp[1] = [0] * 3

        # Traverse each row
        for row in coins:

            # Traverse columns
            for j, x in enumerate(row):

                # -------- Case k = 2 (used 2 skips) --------
                # Options:
                # 1. Continue from left (same row)
                # 2. Continue from top (previous row)
                # 3. Use skip now (coming from k=1)
                dp[j + 1][2] = max(
                    dp[j][2] + x,        # from left, same k
                    dp[j + 1][2] + x,    # from top, same k
                    dp[j][1],            # use skip from left
                    dp[j + 1][1]         # use skip from top
                )

                # -------- Case k = 1 (used 1 skip) --------
                dp[j + 1][1] = max(
                    dp[j][1] + x,        # from left
                    dp[j + 1][1] + x,    # from top
                    dp[j][0],            # use skip from left
                    dp[j + 1][0]         # use skip from top
                )

                # -------- Case k = 0 (no skips used) --------
                # Only option: take the coin value
                dp[j + 1][0] = max(
                    dp[j][0],            # from left
                    dp[j + 1][0]         # from top
                ) + x

        # Return maximum amount using at most 2 skips
        return dp[n][2]