# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

# Example 1:
# Input: cost = [1,2,3]
# Output: 5
# Explanation: We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
# The total cost of buying all candies is 2 + 3 = 5. This is the only way we can buy the candies.
# Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
# The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.

from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total_cost = 0

        # Sort in descending order so the most expensive candies
        # are considered first
        cost.sort(reverse=True)

        l = len(cost)

        # Number of complete groups of 3 candies
        num_three = l // 3

        # Remaining candies after forming groups of 3
        mod_three = l % 3

        pos = 0

        # Process each group of 3 candies
        for i in range(0, num_three):

            # Pay for the most expensive candy
            first_candy = cost[pos]
            total_cost = total_cost + first_candy
            pos += 1

            # Pay for the second most expensive candy
            second_candy = cost[pos]
            total_cost = total_cost + second_candy
            pos += 2

            # Third candy in the group is free,
            # so we skip it by moving pos ahead

        # Add the cost of remaining 1 or 2 candies
        for i in range(0, mod_three):
            candy = cost[pos]
            total_cost = total_cost + candy
            pos += 1

        return total_cost