# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

# Example 1:
# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        xMin = 10**9  # Initialize xMin to a large number (larger than any input element)
        n = len(nums)  # Length of the input list
        maxD = -1  # Initialize the result as -1 (for the case when no increasing pair is found)

        # Traverse each element in the list
        for x in nums:
            if x <= xMin:
                # Update the minimum value seen so far
                xMin = x
            else:
                # If current number is greater than xMin,
                # update maxD with the maximum difference found so far
                maxD = max(maxD, x - xMin)

        return maxD  # Return the maximum difference where the greater element comes after the smaller one
