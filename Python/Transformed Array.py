# https://leetcode.com/problems/transformed-array/

# Example 1:
# Input: nums = [3,-2,1,1]
# Output: [1,1,1,3]
# Explanation:
# For nums[0] that is equal to 3, If we move 3 steps to right, we reach nums[3]. So result[0] should be 1.
# For nums[1] that is equal to -2, If we move 2 steps to left, we reach nums[3]. So result[1] should be 1.
# For nums[2] that is equal to 1, If we move 1 step to right, we reach nums[3]. So result[2] should be 1.
# For nums[3] that is equal to 1, If we move 1 step to right, we reach nums[0]. So result[3] should be 3.

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # Create a copy of nums to store the result
        ans = nums[:]

        # For each index, jump nums[i] steps forward (circularly)
        for i in range(len(nums)):
            ans[i] = nums[(i + nums[i]) % len(nums)]

        return ans
