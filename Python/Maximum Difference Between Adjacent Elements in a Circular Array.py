# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

# Example 1:
# Input: nums = [1,2,4]
# Output: 3
# Explanation:
# Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)

        # Initialize maxa with the absolute difference between the first and last elements
        maxa = abs(nums[0] - nums[-1])

        # Iterate through the array to find the maximum absolute difference 
        # between any two adjacent elements
        for i in range(n - 1):
            maxa = max(maxa, abs(nums[i] - nums[i + 1]))

        # Return the maximum found distance
        return maxa
