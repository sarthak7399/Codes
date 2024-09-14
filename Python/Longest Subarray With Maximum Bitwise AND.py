# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

# Example 1:
# Input: nums = [1,2,3,3,2,2]
# Output: 2
# Explanation:
# The maximum possible bitwise AND of a subarray is 3.
# The longest subarray with that value is [3,3], so we return 2.

from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Get the maximum value from the input array
        max_value = max(nums)
        
        # Initialize current count of consecutive max elements and the longest count found
        current_count = 0
        longest_count = 1
        
        # Loop through the array to find the longest subarray with max_value
        for num in nums:
            if num == max_value:
                # Increment the current count if the number matches the max_value
                current_count += 1
                # Update the longest count if the current streak is longer
                longest_count = max(longest_count, current_count)
            else:
                # Reset current count if the number doesn't match the max_value
                current_count = 0
        
        return longest_count
