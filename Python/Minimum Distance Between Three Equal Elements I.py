# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

# Example 1:
# Input: nums = [1,2,1,1,3]
# Output: 6
# Explanation:
# The minimum distance is achieved by the good tuple (0, 2, 3).
# (0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = defaultdict(list)  # Map each value to the list of its indices
        n = len(nums)

        # Store indices for each value
        for i in range(n):
            mp[nums[i]].append(i)

        ans = float('inf')  # Initialize answer with infinity

        # Process each group of indices (same values)
        for indices in mp.values():
            # We need at least 3 occurrences to form a valid triplet
            if len(indices) < 3:
                continue

            # Check all consecutive triplets of indices
            for i in range(len(indices) - 2):
                # Distance formula:
                # For indices i, j, k → cost = (k - i) + (k - i) = 2 * (k - i)
                dist = 2 * (indices[i + 2] - indices[i])

                # Update minimum distance
                ans = min(ans, dist)

        # If no valid triplet found, return -1
        return -1 if ans == float('inf') else ans