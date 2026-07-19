# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize binary search boundaries
        low = 0
        high = len(nums) - 1

        # Perform modified binary search
        while low <= high:

            # Calculate middle index
            mid = low + (high - low) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[low] <= nums[mid]:

                # Target lies within sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                # Otherwise search right half
                else:
                    low = mid + 1

            # Otherwise right half must be sorted
            else:

                # Target lies within sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

                # Otherwise search left half
                else:
                    high = mid - 1

        # Target not found
        return -1