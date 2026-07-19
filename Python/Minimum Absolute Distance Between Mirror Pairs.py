# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

# Example 1:
# Input: nums = [12,21,45,33,54]
# Output: 1
# Explanation:
# The mirror pairs are:
# (0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
# (2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
# The minimum absolute distance among all pairs is 1.

from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        res = 100000  # Initialize with a large value (acts like infinity)
        seen = {}     # Dictionary to store reversed number → latest index

        # Traverse the array
        for i, n in enumerate(nums):
            
            # If current number exists in 'seen',
            # it means we previously saw its reverse
            if n in seen:
                # Update minimum distance
                res = min(res, i - seen[n])

            # Store the reversed form of current number with its index
            # Example: 123 → 321
            seen[int(str(n)[::-1])] = i

        # If no valid pair found, return -1
        # Trick: -(True) = -1, -(False) = 0 → so result becomes -1 or res
        return -(res == 100000) | res