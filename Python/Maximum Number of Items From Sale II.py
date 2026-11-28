# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

# Example 1:
# Input: items = [[1,6],[2,4],[3,5]], budget = 19
# Output: 5
# Explanation:
# You can buy 2 copies of item 0 and 1 copy of item 1 for a total cost of 2 * 6 + 4 = 16, which is not greater than budget = 19.
# One purchased copy of item 0 gives 1 free copy of item 1, because factor0 = 1 divides factor1 = 2.
# The other purchased copy of item 0 gives 1 free copy of item 2, because factor0 = 1 divides factor2 = 3.
# You leave with 3 purchased copies and 2 free copies, for a total of 5 item copies.

from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # cnt[f] stores the number of items having factor f
        cnt = [0] * (n + 1)

        # Count the frequency of each factor
        for f, p in items:
            cnt[f] += 1

        # mult[f] stores the total number of items whose factors
        # are multiples of f
        mult = [0] * (n + 1)

        # Calculate the count of multiples for every factor
        for f in range(1, n + 1):
            for m in range(f, n + 1, f):
                mult[f] += cnt[m]

        # Find the minimum price among all items
        min_p = min(p for f, p in items)

        # Store candidate items as (price, additional gain) pairs
        cand = []

        for f, p in items:
            # Exclude the item itself to get the additional gain
            # from buying its first copy
            g = mult[f] - 1

            # Consider only items that provide a positive additional gain
            if g > 0:
                cand.append((p, g))

        # Sort candidates by price to prioritise cheaper options
        cand.sort()

        spent = 0   # Total budget spent so far
        total = 0   # Total number of items obtained
        B = budget  # Store the original budget

        # Process candidate items in increasing order of price
        for p, g in cand:

            # Stop if the item costs more than twice the cheapest price
            if p > 2 * min_p:
                break

            # Calculate how many copies can be purchased
            # without exceeding their available gain or remaining budget
            can = min(g, (B - spent) // p)

            # Each selected copy contributes 2 items
            total += can * 2

            # Update the total amount spent
            spent += can * p

        # Use the remaining budget to purchase items at the cheapest price
        total += (B - spent) // min_p

        # Return the maximum number of items obtainable
        return total