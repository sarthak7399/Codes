# https://leetcode.com/problems/smallest-number-with-all-set-bits/

# Example 1:
# Input: n = 5
# Output: 7
# Explanation:
# The binary representation of 7 is "111".

class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        Finds the smallest number that is the sum of distinct powers of 2 (1, 2, 4, 8, ...)
        which is greater than or equal to the given integer `n`.

        Essentially, it keeps adding powers of 2 (2^0, 2^1, 2^2, ...) 
        until the cumulative sum reaches or exceeds `n`.
        """

        result = 0  # Stores cumulative sum of powers of 2
        i = 0       # Power index (starts from 0 → 2^0 = 1)

        # Keep adding powers of 2 until result >= n
        while result < n:
            result += 2 ** i  # Add 2^i to the result
            i += 1            # Move to next power of 2

        return result  # Return the smallest sum ≥ n
