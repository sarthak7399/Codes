# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

# Example 1:
# Input: nums = [0,3,2,1]
# Output: 1
# Explanation:
# Choose k = 1. Swapping nums[1] = 3 and nums[3] = 1 is allowed since nums[1] AND nums[3] == 1, resulting in a sorted permutation: [0, 1, 2, 3].

from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1  # all bits set: nothing misplaced yet
        for i, x in enumerate(nums):
            if x != i:  # this number has to move
                k &= x  # keep only the bits it shares
                if not k:  # bits only disappear, so 0 stays 0
                    return 0
        return max(k, 0)  # -1 means nothing has to move