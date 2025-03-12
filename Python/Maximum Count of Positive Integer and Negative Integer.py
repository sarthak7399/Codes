# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

# Example 1:
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Count negative numbers (index of first 0)
        neg_count = self.binary_search(nums, 0)  
        
        # Count positive numbers (total elements - index of first positive number)
        pos_count = len(nums) - self.binary_search(nums, 1)  
        
        # Return the maximum count
        return max(neg_count, pos_count)

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        result = len(nums)  # Default result if target is not found
        
        # Binary search to find the first index where nums[index] >= target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1  # Search right half
            else:
                result = mid  # Potential answer, search left half for earlier occurrence
                right = mid - 1 
        
        return result  # First occurrence of target or index where it should be inserted
