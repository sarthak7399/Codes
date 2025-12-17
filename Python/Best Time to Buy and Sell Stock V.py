# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

# Example 1:
# Input: prices = [1,7,9,8,2], k = 2
# Output: 14
# Explanation:
# We can make $14 of profit through 2 transactions:
# A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
# A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # Initialise DP for each transaction:
        # dp[t][0] → max profit after t transactions, holding nothing
        # dp[t][1] → max profit after t transactions, holding a bought stock
        # dp[t][2] → max profit after t transactions, holding a sold position
        first_price = prices[0]
        dp = [[0, -first_price, first_price] for _ in range(k + 1)]
        n = len(prices)
        
        # Iterate over days
        for day in range(1, n):
            curr_price = prices[day]
            # Iterate transactions in reverse to avoid overwrite
            for trans in range(k, 0, -1):
                prev_profit = dp[trans - 1][0]
                
                # Update no-stock state: do nothing, sell bought stock, or buy after sell
                dp[trans][0] = max(
                    dp[trans][0],
                    dp[trans][1] + curr_price,
                    dp[trans][2] - curr_price
                )
                
                # Update holding-buy state
                dp[trans][1] = max(dp[trans][1], prev_profit - curr_price)
                
                # Update holding-sell state
                dp[trans][2] = max(dp[trans][2], prev_profit + curr_price)
        
        # Maximum profit after at most k transactions
        return dp[k][0]
