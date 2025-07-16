# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/


# Example 1:
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = max(nums)  # Find the maximum element in the array
        count = 0           # To store the number of valid subarrays
        l = 0               # Left pointer for the sliding window
        max_found = 0       # Number of times the maximum element is found in the current window
        n = len(nums)       # Length of the array

        for r in range(n):  # Iterate with the right pointer
            if nums[r] == max_el:
                max_found += 1  # Track how many max elements are in the window

            # While the current window contains exactly k max elements
            while max_found == k:
                # All subarrays starting from 'l' and ending at any position from 'r' to 'n-1' are valid
                count += n - r

                # Shrink the window from the left
                if nums[l] == max_el:
                    max_found -= 1  # Adjust the count of max elements
                l += 1  # Move the left pointer to the right

        return count
