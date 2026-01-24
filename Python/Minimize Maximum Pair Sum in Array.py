# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

# Example 1:
# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # This will store the maximum pair sum we get
        res = 0

        # Two pointers: l starts from beginning, r from end
        l = 0
        r = len(nums) - 1

        # Sort the array so we can pair smallest with largest
        nums.sort()

        # Keep pairing until pointers meet
        while l < r:
            # Form a pair using smallest and largest remaining numbers
            res = max(res, nums[l] + nums[r])

            # Move pointers inward
            l += 1
            r -= 1

        # Return the maximum pair sum among all pairs
        return res
