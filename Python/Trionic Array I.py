# https://leetcode.com/problems/trionic-array-i/

# Example 1:
# Input: nums = [1,3,5,4,2,6]
# Output: true
# Explanation:
# Pick p = 2, q = 4:
# nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
# nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
# nums[4...5] = [2, 6] is strictly increasing (2 < 6).

from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        # peak: index where increasing stops (first non-increase from left)
        peak = n - 1

        # valley: index where decreasing stops from the right
        valley = 0

        # Scan from both ends simultaneously
        for i in range(n - 1):

            # Find peak point (left to right)
            if peak == n - 1 and nums[i] >= nums[i + 1]:
                peak = i

            # Find valley point (right to left)
            if valley == 0 and nums[-1 - i] <= nums[-2 - i]:
                valley = n - 1 - i

            # Once peak is before valley, check middle part
            if peak < valley:
                return self.isDecreasing(nums, peak, valley)

        return False

    def isDecreasing(self, A: List[int], a: int, b: int) -> bool:
        # Peak cannot be at start and valley cannot be at end
        if a == 0 or b == len(A) - 1:
            return False

        # Check strictly decreasing sequence from a to b
        for i in range(a, b):
            if A[i] <= A[i + 1]:
                return False

        return True
