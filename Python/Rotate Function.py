# https://leetcode.com/problems/rotate-function/

# Example 1:
# Input: nums = [4,3,2,6]
# Output: 26
# Explanation:
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total_sum = 0  # Sum of all elements
        F = 0          # Rotate function value for initial configuration
        
        # Compute total sum and initial rotation value F(0)
        for i in range(n):
            total_sum += nums[i]
            F += i * nums[i]
        
        result = F  # Store maximum rotation value
        
        # Compute rotated function values using recurrence relation:
        # F(k) = F(k-1) + total_sum - n * nums[n-k]
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]

            # Update maximum value
            result = max(result, F)
        
        return result