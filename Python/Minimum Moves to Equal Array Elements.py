# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

# Example 1:
# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

class Solution:
    def minMoves(self, nums):
        # Find the minimum element in the array.
        mn = min(nums)

        # Each move increments n-1 elements by 1.
        # This is equivalent to decrementing one element by 1.
        # Therefore, make every element equal to the minimum value.
        # The total number of moves is the sum of differences from the minimum.
        return sum(nums) - len(nums) * mn