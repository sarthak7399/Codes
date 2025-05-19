# https://leetcode.com/problems/type-of-triangle/description/

# Example 1:
# Input: nums = [3,3,3]
# Output: "equilateral"
# Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.

from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # First, check if the three sides can form a valid triangle
        # Triangle Inequality Theorem: Sum of any two sides must be greater than the third side
        if nums[0] + nums[1] <= nums[2] or \
           nums[1] + nums[2] <= nums[0] or \
           nums[0] + nums[2] <= nums[1]:
            return 'none'  # Not a valid triangle

        # Use a set to identify how many unique side lengths there are
        k = set(nums)

        # All three sides are equal
        if len(k) == 1:
            return 'equilateral'
        # Exactly two sides are equal
        elif len(k) == 2:
            return 'isosceles'
        # All sides are of different lengths
        else:
            return 'scalene'
