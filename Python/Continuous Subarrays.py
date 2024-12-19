# https://leetcode.com/problems/continuous-subarrays/

# Example 1:
# Input: nums = [5,4,2,4]
# Output: 8
# Explanation: 
# Continuous subarray of size 1: [5], [4], [2], [4].
# Continuous subarray of size 2: [5,4], [4,2], [2,4].
# Continuous subarray of size 3: [4,2,4].
# Thereare no subarrys of size 4.
# Total continuous subarrays = 4 + 3 + 1 = 8.
# It can be shown that there are no more continuous subarrays.

from typing import List
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        start = 0  # Start pointer of the sliding window
        total_subarrays = 0  # Total count of valid subarrays
        last_seen = {}  # Dictionary to track the last seen index of each number

        for end, num in enumerate(nums):  # Iterate through nums with the end pointer
            # Create a copy of the dictionary to iterate over while modifying it
            for key, last_index in last_seen.copy().items():
                # If the difference between the current number and key exceeds 2
                if abs(key - num) > 2:
                    # Update the start pointer to exclude invalid elements
                    start = max(start, last_index + 1)
                    # Remove the invalid key from the dictionary
                    last_seen.pop(key)

            # Update the last seen index of the current number
            last_seen[num] = end

            # Add the count of valid subarrays ending at the current position
            total_subarrays += end - start + 1

        return total_subarrays
