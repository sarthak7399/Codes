# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

# Example 1:
# Input: items = [[6,2],[2,6],[3,4]], budget = 9
# Output: 4
# Explanation:
# You can buy 2 copies of item 0 and 1 copy of item 2 for a total cost of 2 * 2 + 4 = 8, which is not greater than budget = 9.
# Buying item 2 gives 1 free copy of item 0, because factor2 = 3 divides factor0 = 6.
# You leave with 3 purchased copies and 1 free copy, for a total of 4 item copies.

from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # Separate item factors and prices
        factors, prices = zip(*items)

        # have[f] stores the number of items having factor f
        have = [0] * (max(factors) + 1)

        # Count the frequency of each factor
        for factor in factors:
            have[factor] += 1

        # Calculate the total gain for each unique factor
        # Every multiple of a factor contributes to its gain
        gains = {
            factor: sum(have[factor::factor])
            for factor in set(factors)
        }

        # Find the minimum item price
        cheapest = min(prices)

        # Initialise DP assuming all money is spent on the cheapest item
        # best[money] stores the maximum number of items obtainable
        # with the given amount of money, without buying first copies
        best = [money // cheapest for money in range(budget + 1)]

        # Process each item as a 0/1 knapsack choice
        for factor, price in items:

            # Get the gain associated with the current item's factor
            # Skip if buying its first copy is not better than
            # spending the same amount on the cheapest item
            if (gain := gains[factor]) > price // cheapest:

                # Traverse budgets backwards to ensure each item
                # contributes at most one first copy
                for money in range(budget, price - 1, -1):

                    # Either keep the existing maximum or buy
                    # the current item's first copy and add its gain
                    best[money] = max(
                        best[money],
                        best[money - price] + gain
                    )

        # Return the maximum number of items obtainable within the budget
        return best[budget]