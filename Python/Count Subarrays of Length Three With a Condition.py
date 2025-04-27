# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

# Example 1:
# Input: nums = [1,2,1,4,1]
# Output: 1
# Explanation:
# Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0  # Count of Good Squads
        n = len(nums)

        # Check each group of 3 consecutive soldiers
        for i in range(n - 2):
            first = nums[i]
            middle = nums[i + 1]
            third = nums[i + 2]

            # Check if the squad is a Good Squad
            if (first + third) * 2 == middle:
                count += 1  # Good Squad!

        return count  # Return total Good Squads count