# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# Example 1:
# Input: nums = [1,3,5]
# Output: 1

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize binary search boundaries
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left < right:
            mid = (left + right) // 2

            # Minimum lies in the right half
            # because mid element is greater than rightmost element
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum lies in the left half (including mid)
            elif nums[mid] < nums[right]:
                right = mid

            # nums[mid] == nums[right]
            # Cannot determine the side, safely shrink search space
            else:
                right -= 1

        # left points to the minimum element
        return nums[left]