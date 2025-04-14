# https://leetcode.com/problems/partition-equal-subset-sum/

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

from functools import cache
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, we cannot partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2  # The sum we want each subset to have

        @cache
        def can_form_subset(index: int, current_sum: int) -> bool:
            # If we've reached the target sum, a valid subset is found
            if current_sum == target_sum:
                return True
            # If we've used all elements or exceeded the target, stop
            if index < 0 or current_sum > target_sum:
                return False
            # Try including or excluding the current element
            return (
                can_form_subset(index - 1, current_sum + nums[index]) or 
                can_form_subset(index - 1, current_sum)
            )

        # Start from the last index with 0 as the initial subset sum
        return can_form_subset(len(nums) - 1, 0)
