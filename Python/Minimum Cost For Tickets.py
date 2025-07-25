# https://leetcode.com/problems/minimum-cost-for-tickets/

# Example 1:
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total, you spent $11 and covered all the days of your travel.

from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Create a set of travel days for quick lookup
        travel_days = set(days)

        # Initialize a DP array for 365 days
        dp = [0] * 366  # dp[i] is the min cost to travel up to day i

        for i in range(1, 366):
            if i not in travel_days:
                # If it's not a travel day, the cost is the same as the previous day
                dp[i] = dp[i - 1]
            else:
                # Calculate the cost if we buy a 1-day, 7-day, or 30-day pass
                cost1 = dp[i - 1] + costs[0]
                cost7 = dp[max(0, i - 7)] + costs[1]
                cost30 = dp[max(0, i - 30)] + costs[2]
                
                # Take the minimum of the three options
                dp[i] = min(cost1, cost7, cost30)

        # Return the cost to cover all days in the year
        return dp[365]