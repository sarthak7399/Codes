# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

# Example 1:
# Input: nums = [1,2,3]
# Output: 12
# Explanation:
# A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.
# The alternating score is calculated as:
# score = 22 - 12 + 32 = 4 - 1 + 9 = 12

import random

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Square each element.
        sq = [x * x for x in nums]

        # Start with the sum of all squares, then subtract twice
        # the sum of the smallest half to minimize the result.
        return sum(sq) - 2 * self.sum_smallest(sq, len(sq) // 2)

    def sum_smallest(self, a: list[int], k: int) -> int:
        # Return 0 if no elements are needed.
        if k == 0:
            return 0

        # Choose a random pivot to partition the array.
        pivot = random.choice(a)

        # Store elements smaller than the pivot.
        lo = [x for x in a if x < pivot]

        # If the k smallest elements are all below the pivot,
        # recursively find their sum in the smaller partition.
        if k <= len(lo):
            return self.sum_smallest(lo, k)

        # Count how many copies of the pivot are needed.
        take = min(k - len(lo), a.count(pivot))

        # Store elements greater than the pivot.
        hi = [x for x in a if x > pivot]

        # Include all smaller elements, the required pivot copies,
        # and any remaining elements needed from the greater partition.
        return (
            sum(lo)
            + take * pivot
            + self.sum_smallest(hi, k - len(lo) - take)
        )