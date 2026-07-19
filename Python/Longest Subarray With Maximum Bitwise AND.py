# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

# Example 1:
# Input: nums = [1,2,3,3,2,2]
# Output: 2
# Explanation:
# The maximum possible bitwise AND of a subarray is 3.
# The longest subarray with that value is [3,3], so we return 2.

from typing import List

# Method 1 : Brute Force
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


# # Method 2 : Optimized

# from itertools import groupby  # Import groupby for grouping consecutive identical elements

# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         max_ = max(nums)  # Find the maximum value in the list

#         # Group consecutive elements with same value using groupby.
#         # For each group where the key (element value) == max_,
#         # calculate the length of the group (i.e., how many times max_ appears consecutively).
#         # Finally, return the largest such length.
#         return max(
#             len(list(values))        # Length of the current group of max_ values
#             for key, values in groupby(nums)  # key = value, values = iterator of consecutive same values
#             if key == max_           # We care only about groups where value == max_
#         )
