# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

# Example 1:
# Input: nums = [1,2,1,1,3]
# Output: 6
# Explanation:
# The minimum distance is achieved by the good tuple (0, 2, 3).
# (0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}  # Dictionary to store indices for each number
        
        # Build the positions dictionary
        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)
        
        ans = float('inf')  # Initialize answer with infinity
        
        # Iterate over all groups of indices (same numbers)
        for idx in positions.values():
            # Skip if fewer than 3 occurrences
            if len(idx) < 3:
                continue
            
            # Check all consecutive triplets
            for i in range(len(idx) - 2):
                # Calculate distance for triplet:
                # distance = 2 * (last_index - first_index)
                distance = 2 * (idx[i + 2] - idx[i])
                
                # Update minimum distance
                ans = min(ans, distance)
        
        # If no valid triplet found, return -1
        return -1 if ans == float('inf') else ans