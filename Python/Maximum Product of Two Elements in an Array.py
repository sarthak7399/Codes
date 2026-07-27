# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

# Example 1:
# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Store the largest element
        first = 0

        # Store the second largest element
        second = 0

        for num in nums:

            # Update both largest and second largest values
            if num >= first:
                second = first
                first = num

            # Update only the second largest value
            elif num > second:
                second = num

        # Return the required maximum product
        return (first - 1) * (second - 1)