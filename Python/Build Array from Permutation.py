# https://leetcode.com/problems/build-array-from-permutation/

# Example 1:
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows: 
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Given a zero-based permutation array `nums`, 
        # this returns a new array `ans` such that:
        # ans[i] = nums[nums[i]]
        # The result is constructed using list comprehension.
        return [nums[nums[i]] for i in range(len(nums))]
