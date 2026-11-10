# https://leetcode.com/problems/climbing-stairs-ii/

# Example 1:
# Input: n = 4, costs = [1,2,3,4]
# Output: 13
# Explanation:
# One optimal path is 0 → 1 → 2 → 4
# Jump	Cost Calculation	Cost
# 0 → 1	costs[1] + (1 - 0)2 = 1 + 1	2
# 1 → 2	costs[2] + (2 - 1)2 = 2 + 1	3
# 2 → 4	costs[4] + (4 - 2)2 = 4 + 4	8
# Thus, the minimum total cost is 2 + 3 + 8 = 13

from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[j] stores the minimum cost required to reach step j.
        # Initialise all steps with infinity since they are initially unreachable.
        dp = [float('inf')] * (n + 1)

        # Starting from step 0 requires no cost.
        dp[0] = 0

        # Calculate the minimum cost to reach each step from 1 to n.
        for j in range(1, n + 1):

            # A jump can cover 1, 2, or 3 steps.
            for k in range(1, 4):
                # Calculate the previous step from which we jump.
                i = j - k

                # Ensure the previous step is within the valid range.
                if i >= 0:
                    # Jump cost is the square of the number of steps jumped.
                    jump = (j - i) * (j - i)

                    # Update the minimum cost to reach step j.
                    # This includes the cost of reaching step i,
                    # the cost of landing on step j, and the jump cost.
                    dp[j] = min(dp[j], dp[i] + costs[j - 1] + jump)

        # Return the minimum cost required to reach the top step.
        return dp[n]