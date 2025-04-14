# https://leetcode.com/problems/maximum-ascending-subarray-sum/

# Example 1:
# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = current_sum
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]: 
                current_sum += nums[i]  # Extend ascending subarray
            else:
                current_sum = nums[i]  # Start a new subarray
                
            max_sum = max(max_sum, current_sum)  # Update max sum
        
        return max_sum