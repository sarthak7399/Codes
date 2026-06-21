# https://leetcode.com/problems/maximum-ice-cream-bars/

# Example 1:
# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

from collections import Counter
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Count how many ice creams exist for each cost
        cnt = Counter(costs)

        # Stores the maximum number of ice creams purchased
        ans = 0

        # Process costs in increasing order
        # (greedily buy cheaper ice creams first)
        for c in range(1, max(cnt) + 1):

            # Maximum ice creams we can buy at cost c
            buy = min(
                cnt[c],        # available ice creams with cost c
                coins // c     # affordable quantity
            )

            # Add purchased ice creams to answer
            ans += buy

            # Deduct spent coins
            coins -= buy * c

        return ans