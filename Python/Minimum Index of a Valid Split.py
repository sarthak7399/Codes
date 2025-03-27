# https://leetcode.com/problems/minimum-index-of-a-valid-split/

# Example 1:
# Input: nums = [1,2,2,2]
# Output: 2
# Explanation: We can split the array at index 2 to obtain arrays [1,2,2] and [2]. 
# In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3. 
# In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
# Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split. 
# It can be shown that index 2 is the minimum index of a valid split.

from typing import List
class Solution:    
    def minimumIndex(self, nums: List[int]) -> int:    
        from collections import Counter

        # Count the frequency of each number in the list
        freq = Counter(nums)
        n = len(nums)
        dom, count = 0, 0

        # Find the dominant element (if it appears more than n//2 times)
        for num, c in freq.items():
            if c > n // 2:
                dom, count = num, c
                break

        left_count = 0  # Count of dominant element in the left partition

        # Iterate through the list, splitting it into left and right parts
        for i in range(n - 1):
            if nums[i] == dom:
                left_count += 1  # Update dominant element count in the left partition
            
            left_size = i + 1  # Size of the left partition
            right_size = n - left_size  # Size of the right partition
            right_count = count - left_count  # Remaining count of dominant element in the right partition

            # Check if both partitions satisfy the dominant element condition
            if left_count > left_size // 2 and right_count > right_size // 2:
                return i  # Return the index where the split is valid

        return -1  # No valid split found
