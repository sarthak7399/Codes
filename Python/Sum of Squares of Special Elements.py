# https://leetcode.com/problems/sum-of-squares-of-special-elements/

# Example 1:
# Input: nums = [1,2,3,4]
# Output: 21
# Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
# Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  

from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # Initialize the sum of squares.
        ans = 0

        # Get the length of the array.
        n = len(nums)

        # Check each 1-based index from 1 to n.
        for i in range(1, n + 1):
            # If the index divides n, it is a divisor of the array length.
            if n % i == 0:
                # Add the square of the element at index i - 1.
                ans += nums[i - 1] * nums[i - 1]

        # Return the sum of squares of elements at divisor indices.
        return ans
    