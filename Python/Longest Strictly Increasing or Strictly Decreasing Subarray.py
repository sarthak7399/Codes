# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

# Example 1:
# Input: nums = [1,4,3,3,2]
# Output: 2
# Explanation:
# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
# Hence, we return 2.

from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Initialize variables:
        # res stores the length of the longest monotonic subarray found.
        # low and high are counters for the lengths of decreasing and increasing subarrays, respectively.
        # prev keeps track of the previous number in the array for comparison.
        res = low = high = 1
        prev = nums[0]  # Set the first element as the previous number.
        
        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # If the current element is greater than the previous one, it's increasing.
            if nums[i] > prev:
                high += 1  # Increment the count for increasing subarray length.
                low = 1  # Reset decreasing subarray length.
            # If the current element is smaller than the previous one, it's decreasing.
            elif nums[i] < prev:
                low += 1  # Increment the count for decreasing subarray length.
                high = 1  # Reset increasing subarray length.
            # If the current element is equal to the previous one, it's a neutral case.
            else:
                low = 1  # Reset decreasing subarray length.
                high = 1  # Reset increasing subarray length.
            
            # Update the result to the maximum length found so far.
            res = max([res, low, high])
            
            # Update the previous number for the next iteration.
            prev = nums[i]
        
        # Return the length of the longest monotonic subarray found.
        return res
