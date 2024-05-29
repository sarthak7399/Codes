# https://www.geeksforgeeks.org/problems/minimum-cost-to-fill-given-weight-in-a-bag1956/

# Example 1:
# Input: n = 5
# cost[] = {20, 10, 4, 50, 100} 
# w = 5
# Output: 14
# Explanation: 
# Purchase the 2kg packet for 10 coins and the 3kg packet for 4 coins to buy 5kg of oranges for 14 coins.

from typing import List
class Solution:
    def minimumCost(self, n: int, w: int, cost: List[int]) -> int:
        # Initialize dp array with infinity
        dp = [float('inf')] * (w + 1)
        
        # Base case: cost of 0 kg is 0
        dp[0] = 0
        
        # Update dp array
        for i in range(1, w + 1):
            for j in range(1, n + 1):
                if j <= i and cost[j - 1] != -1:
                    dp[i] = min(dp[i], dp[i - j] + cost[j - 1])
        
        # If dp[w] is still infinity, return -1 (not possible to get exactly w kg)
        return -1 if dp[w] == float('inf') else dp[w]