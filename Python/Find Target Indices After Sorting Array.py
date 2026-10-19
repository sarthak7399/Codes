# https://leetcode.com/problems/find-target-indices-after-sorting-array/

# Example 1:
# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Count elements smaller than target.
        # These elements appear before target after sorting.
        left = sum(x < target for x in nums)

        # Count elements smaller than or equal to target.
        # This gives the position just after the last occurrence of target.
        right = sum(x <= target for x in nums)

        # After sorting, target occupies indices from left to right - 1.
        return list(range(left, right))