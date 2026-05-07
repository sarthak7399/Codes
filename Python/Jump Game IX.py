# https://leetcode.com/problems/jump-game-ix/

# Example 1:
# Input: nums = [2,1,3]
# Output: [2,2,3]
# Explanation:
# For i = 0: No jump increases the value.
# For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
# For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
# Thus, ans = [2, 2, 3].

from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # res[i] stores prefix maximum up to index i
        res = [nums[0]]

        # Build prefix maximum array
        for i in range(1, n):
            res.append(max(res[-1], nums[i]))

        # Track index of minimum element from the right
        min_idx = n - 1

        # Traverse from right to left
        for i in range(n - 2, -1, -1):

            # If prefix max is greater than current suffix minimum,
            # replace it with corresponding value from res[min_idx]
            if res[i] > nums[min_idx]:
                res[i] = res[min_idx]

            # Update suffix minimum index
            if nums[i] < nums[min_idx]:
                min_idx = i

        return res