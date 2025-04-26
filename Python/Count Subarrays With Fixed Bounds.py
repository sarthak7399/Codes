# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

# Example 1:
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0                 # Final answer to store the count of valid subarrays
        maxi, mini = -1, -1      # Indices where maxK and minK were last seen
        s, l = len(nums), 0      # s = length of nums, l = left boundary of the valid window

        for r, x in enumerate(nums):  # r = right pointer, x = current element
            if x < minK or x > maxK:
                l = r + 1       # If out of valid range, reset left boundary after r
                continue

            if x == maxK:
                maxi = r        # Update last seen index of maxK
            if x == minK:
                mini = r        # Update last seen index of minK

            # The number of valid subarrays ending at r is based on the earlier of the two indices
            ans += max((min(maxi, mini) - l + 1), 0)

        return ans
