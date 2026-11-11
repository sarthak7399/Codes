# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

# Example 1:
# Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2
# Output: 3
# Explanation:
# After buying three type 3 items, which cost 3 * 1 = 3, the total contribution to type 1 is 3 (>= need1 = 3) and to type 2 is 3 (>= need2 = 2).
# Any other valid combination would cost more, so the minimum total cost is 3.

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Store the individual and combined costs in shorter variable names.
        c1, c2, cb = cost1, cost2, costBoth
        n1, n2 = need1, need2

        # Find the maximum number of units that can satisfy both requirements.
        pairs = min(n1, n2)

        # For each pair, choose the cheaper option:
        # either buy both together or buy them separately.
        cost_pairs = pairs * min(cb, c1 + c2)

        # Calculate the remaining individual requirements after satisfying pairs.
        rem1 = n1 - pairs
        rem2 = n2 - pairs

        # For the remaining units, choose the cheaper option:
        # buy the required item individually or use the combined purchase.
        cost_rem = rem1 * min(c1, cb) + rem2 * min(c2, cb)

        # Return the total minimum cost.
        return cost_pairs + cost_rem