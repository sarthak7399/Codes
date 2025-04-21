# https://leetcode.com/problems/count-the-hidden-sequences/

# Example 1:
# Input: differences = [1,-3,4], lower = 1, upper = 6
# Output: 2
# Explanation: The possible hidden sequences are:
# - [3, 4, 1, 5]
# - [4, 5, 2, 6]
# Thus, we return 2.

from typing import List

class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        a = 0           # Cumulative sum starting from 0 (acts as the initial element of the original array)
        maxima = 0      # Will track the maximum value reached in the cumulative sum
        minima = 0      # Will track the minimum value reached in the cumulative sum

        # Iterate through the differences to simulate the original array
        for d in diff:
            a += d                      # Add the difference to the current sum
            maxima = max(maxima, a)    # Update the maximum value seen so far
            minima = min(minima, a)    # Update the minimum value seen so far

        # The original array can start from any value 'x' such that:
        # x + minima >= lower and x + maxima <= upper
        # So, the valid range for x is: [lower - minima, upper - maxima]
        # The count of such valid starting values = (upper - lower) - (maxima - minima) + 1

        return max(0, (upper - lower) - (maxima - minima) + 1)  # Ensure non-negative result
