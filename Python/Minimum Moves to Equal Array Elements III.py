# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

# Example 1:
# Input: nums = [2,1,3]
# Output: 3
# Explanation:
# To make all elements equal:
# Increase nums[0] = 2 by 1 to make it 3.
# Increase nums[1] = 1 by 1 to make it 2.
# Increase nums[1] = 2 by 1 to make it 3.
# Now, all elements of nums are equal to 3. The minimum total moves is 3.

class Solution:
    def minMoves(self, nums):
        # Find the maximum element and assume all elements
        # need to be increased to this value.
        # Calculate the total increments required.
        # Each move increments exactly one element by 1.
        return max(nums) * len(nums) - sum(nums)