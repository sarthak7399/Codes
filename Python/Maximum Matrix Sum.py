# https://leetcode.com/problems/maximum-matrix-sum/

# Example 1:
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0            # Sum of absolute values
        negative_count = 0       # Count of negative numbers
        min_abs_value = float('inf')  # Smallest absolute value in matrix
        
        for row in matrix:
            for value in row:
                total_sum += abs(value)   # Add absolute value
                if value < 0:
                    negative_count += 1   # Track negatives
                min_abs_value = min(min_abs_value, abs(value))
        
        # If negatives are odd, one value must remain negative
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value
        
        return total_sum
