# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

# Example 1:
# Input: nums = [10,12,13,14]
# Output: 1
# Explanation:
# nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        # Initialize answer with a very large value
        ans = float('inf')

        # Traverse each number in the array
        for num in nums:

            total = 0  # Stores sum of digits of current number

            # Calculate digit sum
            while num > 0:
                total += (num % 10)  # Add last digit
                num //= 10           # Remove last digit

            # Update minimum digit sum found so far
            ans = min(ans, total)

        return ans