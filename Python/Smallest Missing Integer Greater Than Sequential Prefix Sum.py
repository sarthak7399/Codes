# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

# Example 1:
# Input: nums = [1,2,3,2,5]
# Output: 6
# Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Start with the first element of the array.
        # This represents the sum of the longest sequential prefix.
        total = nums[0]

        # Find the longest prefix where every element is
        # exactly one greater than the previous element.
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                # Stop as soon as the consecutive sequence breaks.
                break

        # Store all elements for O(1) average-time lookup.
        seen = set(nums)

        # Start checking from the sum of the sequential prefix.
        answer = total

        # If the sum already exists in the array, keep incrementing
        # until we find the smallest missing integer.
        while answer in seen:
            answer += 1

        return answer