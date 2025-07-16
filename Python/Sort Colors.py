# https://leetcode.com/problems/sort-colors/

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort the input list nums in-place such that all 0s come first,
        followed by all 1s, then all 2s.
        This is a counting sort approach optimized for three unique values (0, 1, 2).
        """
        zeros, ones, n = 0, 0, len(nums)

        # First pass: count number of 0s and 1s (since remaining will be 2s)
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1

        # Second pass: overwrite the list with the counted number of 0s
        for i in range(0, zeros):
            nums[i] = 0

        # Fill next segment with 1s
        for i in range(zeros, zeros + ones):
            nums[i] = 1

        # Fill remaining with 2s
        for i in range(zeros + ones, n):
            nums[i] = 2
