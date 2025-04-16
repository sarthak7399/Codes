# https://leetcode.com/problems/count-the-number-of-good-subarrays/

# Example 2:
# Input: nums = [3,1,4,3,2,2,4], k = 2
# Output: 4
# Explanation: There are 4 different good subarrays:
# - [3,1,4,3,2,2] that has 2 pairs.
# - [3,1,4,3,2,2,4] that has 3 pairs.
# - [1,4,3,2,2,4] that has 2 pairs.
# - [4,3,2,2,4] that has 2 pairs.

from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Dictionary to store frequency of elements in the current window
        freq = defaultdict(int)
        
        left = 0              # Left pointer of the sliding window
        pair_count = 0        # Count of good pairs in the current window
        good_subarrays = 0    # Total number of good subarrays

        # Iterate through the array using the right pointer
        for right in range(len(nums)):
            # Add the number of pairs that can be formed with nums[right]
            pair_count += freq[nums[right]]
            
            # Increment frequency of the current number
            freq[nums[right]] += 1

            # Shrink the window from the left while pair_count is at least k
            while pair_count >= k:
                # All subarrays from left to right are good if current pair_count ≥ k
                # So, we add (len(nums) - right) to count all such subarrays
                good_subarrays += len(nums) - right

                # Remove nums[left] from window and adjust pair_count
                freq[nums[left]] -= 1
                pair_count -= freq[nums[left]]  # Subtract remaining frequency after decrement
                left += 1  # Move the window forward

        return good_subarrays
