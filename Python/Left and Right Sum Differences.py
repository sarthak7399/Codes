# https://leetcode.com/problems/left-and-right-sum-differences/

# Example 1:
# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Total sum of all elements (initial right sum)
        right_sum = sum(nums)

        # Running sum of elements to the left
        left_sum = 0

        # Stores the answer for each index
        result = []

        # Traverse the array
        for num in nums:

            # Remove current element from right sum
            # so right_sum contains sum of elements strictly to the right
            right_sum -= num

            # Store absolute difference between
            # left-side sum and right-side sum
            result.append(abs(left_sum - right_sum))

            # Add current element to left sum
            # for the next iteration
            left_sum += num

        return result