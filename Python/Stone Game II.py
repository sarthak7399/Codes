# https://leetcode.com/problems/stone-game-ii/

# Example 1:
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Number of piles
        n = len(piles)

        # dp[i][m] = maximum stones the current player can collect
        # starting from index i when the current M value is m.
        dp = [[0] * (n + 1) for _ in range(n)]

        # suffix_sum[i] = total number of stones from index i to the end.
        # This allows us to calculate the total remaining stones in O(1).
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Process states from the end of the array towards the beginning.
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):

                # If the player can take all remaining piles,
                # they simply collect all remaining stones.
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]

                else:
                    # Try taking x piles, where 1 <= x <= 2 * m.
                    for x in range(1, 2 * m + 1):

                        # Current player gets all remaining stones
                        # minus the maximum stones the opponent can
                        # collect from the next state.
                        #
                        # The new M value becomes max(m, x).
                        dp[i][m] = max(
                            dp[i][m],
                            suffix_sum[i] -
                            dp[i + x][max(m, x)]
                        )

        # Initially, the game starts at index 0 with M = 1.
        return dp[0][1]