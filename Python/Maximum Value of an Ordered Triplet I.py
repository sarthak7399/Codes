# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

# Example 1:
# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77.

from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        L = [0] * n  # L[i] stores the maximum value encountered from the left up to index i
        R = [0] * n  # R[i] stores the maximum value encountered from the right up to index i
        
        # Populate L: Track the maximum value from the left side
        for i in range(n - 1):
            L[i + 1] = max(L[i], nums[i])
        
        # Populate R: Track the maximum value from the right side
        for i in range(n - 1):
            R[n - 2 - i] = max(R[n - i - 1], nums[n - i - 1])
        
        # Compute the maximum triplet value using the formula (L[i] - nums[i]) * R[i]
        return max(0, max((L[i] - nums[i]) * R[i] for i in range(1, n - 1)))
