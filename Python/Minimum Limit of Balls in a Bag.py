# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

# Example 1:
# Input: nums = [9], maxOperations = 2
# Output: 3
# Explanation: 
# - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
# - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
# The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

from math import ceil
from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Helper function to check if we can divide all numbers
        # in the array such that the largest ball count in any bag is <= maxBalls
        def can_divide(max_balls_per_bag):
            operations_used = 0  # Count of operations performed
            for ball_count in nums:
                # Calculate the required operations to divide the balls
                operations_used += ceil(ball_count / max_balls_per_bag) - 1
                # If operations exceed the allowed limit, division is not feasible
                if operations_used > maxOperations:
                    return False
            return True

        # Binary search for the smallest possible maximum ball count per bag
        left, right = 1, max(nums)  # Search range: 1 to max number in the array
        result = right  # Initialize result to the maximum value in nums

        while left < right:
            mid = left + ((right - left) // 2)  # Calculate the middle value
            if can_divide(mid):  # Check if it's feasible to divide with this max value
                right = mid  # Update the upper bound
                result = right  # Store the current feasible result
            else:
                left = mid + 1  # Update the lower bound if not feasible

        return result  # Return the smallest possible maximum value
