# https://leetcode.com/problems/zero-array-transformation-i/

# Example 1:
# Input: nums = [1,0,1], queries = [[0,2]]
# Output: true
# Explanation:
# For i = 0:
# Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
# The array will become [0, 0, 0], which is a Zero Array.

from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)

        # Step 1: Create a difference array for applying range updates efficiently
        diff = [0] * (n + 1)

        # Step 2: Apply each query as a range decrement
        for li, ri in queries:
            # Decrement start of range
            diff[li] -= 1
            # Cancel the effect after the end of range (only if within bounds)
            if ri + 1 < n:
                diff[ri + 1] += 1

        # Step 3: Accumulate the difference array to get final values
        sum_val = 0
        for i in range(n):
            sum_val += diff[i]

            # nums[i] must be at least equal to -sum_val (we're subtracting values)
            if nums[i] > -sum_val:
                return False  # Not enough decrements to make nums[i] zero or less

        # If all elements can be reduced to zero or below
        return True
