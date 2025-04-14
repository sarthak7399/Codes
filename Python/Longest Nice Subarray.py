# https://leetcode.com/problems/longest-nice-subarray/

# Example 1:
# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 1  # Stores the maximum length of a nice subarray
        
        left = 0  # Left pointer of the sliding window
        used_bits = 0  # Tracks the bitwise OR of elements in the current window
        
        for right in range(n):
            # If nums[right] has any common bits with used_bits, shrink the window
            while used_bits & nums[right] != 0:
                used_bits ^= nums[left]  # Remove nums[left] from the bitmask
                left += 1  # Move left pointer
            
            # Include nums[right] in the window
            used_bits |= nums[right]
            
            # Update the max length of the nice subarray
            max_length = max(max_length, right - left + 1)
            
        return max_length
