# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

# Example 1:
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Sort the array to find the median.
        nums.sort()

        # The median minimises the total absolute difference
        # when making all elements equal.
        median = nums[len(nums) // 2]

        # Calculate the total moves required to make every element equal to the median.
        moves = 0
        for num in nums:
            # Each element needs |num - median| moves to reach the median.
            moves += abs(num - median)

        # Return the minimum total number of moves.
        return moves