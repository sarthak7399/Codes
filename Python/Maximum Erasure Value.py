# https://leetcode.com/problems/maximum-erasure-value/

# Example 1:
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].

from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()            # Set to store unique elements currently in the window
        left = 0                # Left boundary of the sliding window
        current_sum = 0         # Current sum of elements in the window
        max_sum = 0             # Maximum sum found so far
        
        for right in range(len(nums)):  # Iterate with the right boundary
            # If we encounter a duplicate, move the left boundary forward
            # until the duplicate is removed
            while nums[right] in seen:
                current_sum -= nums[left]   # Remove nums[left] from sum
                seen.remove(nums[left])     # Remove nums[left] from set
                left += 1                   # Move left pointer to the right

            # Add current number to sum and mark as seen
            current_sum += nums[right]
            seen.add(nums[right])

            # Update maximum sum if needed
            max_sum = max(max_sum, current_sum)
        
        return max_sum  # Return the maximum sum of a subarray with unique elements
