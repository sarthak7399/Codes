# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

# Example 1:
# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following: 
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.

from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the 2D grid into a 1D list
        all_nums = [num for row in grid for num in row]
        
        # Check if all elements have the same remainder when divided by x
        mod = all_nums[0] % x
        if any(num % x != mod for num in all_nums):
            return -1  # If not, transformation is impossible

        # Sort the numbers to find the median efficiently
        all_nums.sort()
        median = all_nums[len(all_nums) // 2]  # Median minimizes total operations

        # Calculate the total operations needed to make all elements equal to the median
        return sum(abs(num - median) // x for num in all_nums)
