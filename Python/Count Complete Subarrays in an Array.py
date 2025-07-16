# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

# Example 1:
# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Total number of unique elements in the input list
        total_unique = len(set(nums))
        
        count = 0      # To store the count of complete subarrays
        left = 0       # Left pointer of the sliding window
        freq = {}      # Frequency map for current window elements

        for right in range(len(nums)):
            # Add the current element at 'right' to the frequency map
            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1
                
            # Shrink the window from the left while it contains all unique elements
            while len(freq) == total_unique:
                # All subarrays from current 'left' to end of array are valid
                count += len(nums) - right

                # Remove or decrement the count of the leftmost element
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]  # Remove from map if count is 0
                left += 1  # Move the left pointer forward

        return count
