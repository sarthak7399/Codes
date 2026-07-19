# https://leetcode.com/problems/rearranging-fruits/

# Example 1:
# Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
# Output: 1
# Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.

from typing import Counter

class Solution:
    def minCost(self, basket1, basket2):
        count = Counter()                # To keep track of surplus and deficit of each fruit/item
        global_min = float('inf')        # To store the minimum value among all items across both baskets

        # Step 1: Count the difference in quantities and track global minimum item value
        for x in basket1:
            count[x] += 1                # basket1 adds to the count
            global_min = min(global_min, x)
        for x in basket2:
            count[x] -= 1                # basket2 reduces from the count
            global_min = min(global_min, x)

        total = 0

        # Step 2: Check if it's possible to balance baskets by swapping
        # If for any item, difference is odd, it means balancing is impossible
        for v in count.values():
            if v % 2 != 0:
                return -1  # Can't swap to make equal
            total += abs(v)   # Count total number of surplus/deficit items

        # Step 3: Build list of items that need to be swapped (half of the surplus/deficit)
        im = []
        for num, v in count.items():
            im.extend([num] * (abs(v) // 2))

        # Step 4: Sort the swap list so that cheaper items come first
        im.sort()

        # Step 5: Find the cost of swaps
        # Only need to do half of the swaps, as each swap fixes two differences
        # Choose between directly swapping item or swapping via two global_min items (which may be cheaper)
        half = len(im) // 2
        double_min = 2 * global_min
        ans = sum(min(im[i], double_min) for i in range(half))

        # Step 6: Return the final answer (minimum cost to balance baskets)
        return ans
