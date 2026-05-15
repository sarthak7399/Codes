# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # Binary search to find minimum element
        while l < r:

            # Middle index
            mid = (l + r) // 2

            # If middle element is smaller than rightmost element,
            # minimum lies in left half (including mid)
            if nums[mid] < nums[r]:
                r = mid

            # Otherwise, minimum lies in right half
            else:
                l = mid + 1

        # l (or r) points to the minimum element
        return nums[l]
    