# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

# Example 1:
# Input: prices = [4,2,8], strategy = [-1,0,1], k = 2
# Output: 10
# Explanation:
# Modification	Strategy	Profit Calculation	Profit
# Original	[-1, 0, 1]	(-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8	4
# Modify [0, 1]	[0, 1, 1]	(0 × 4) + (1 × 2) + (1 × 8) = 0 + 2 + 8	10
# Modify [1, 2]	[-1, 0, 1]	(-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8	4
# Thus, the maximum possible profit is 10, which is achieved by modifying the subarray [0, 1]​​​​​​​.

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # Apply strategy multiplier to prices
        sp = [s * p for s, p in zip(strategy, prices)]
        n = len(prices)

        # Baseline profit using original strategy
        baseline = sum(sp)

        # Half window size
        h = k // 2

        # Initial window sums
        old = sum(sp[:k])              # strategy-based sum
        new = sum(prices[h:k])         # modified strategy sum

        # Track maximum improvement
        maxdiff = max(0, new - old)

        # Slide window across prices
        for r in range(k, n):
            l = r - k + 1
            old += sp[r] - sp[l - 1]           # update old window sum
            new += prices[r]                   # add new right element
            new -= prices[l - 1 + h]           # remove left element of half window
            maxdiff = max(maxdiff, new - old)

        # Return best possible profit
        return baseline + maxdiff
