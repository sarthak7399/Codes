# https://leetcode.com/problems/minimum-score-by-changing-two-elements/

# Example 1:
# Input: nums = [1,4,7,8,5]
# Output: 3
# Explanation:
# Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
# The low score is the minimum absolute difference: |6 - 6| = 0.
# The high score is the maximum absolute difference: |8 - 5| = 3.
# The sum of high and low score is 3.

from heapq import nlargest, nsmallest
from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Find the 3 smallest elements in the array
        small = nsmallest(3, nums)

        # Find the 3 largest elements in the array
        large = nlargest(3, nums)

        # Calculate the minimum possible difference after removing
        # any 2 elements from the array
        return min(
            large[0] - small[2],  # Remove the 2 largest elements
            large[1] - small[1],  # Remove the largest and smallest elements
            large[2] - small[0]   # Remove the 2 smallest elements
        )