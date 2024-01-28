# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0

        # Calculate the product of all elements and count the number of zeros
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_count += 1

        # If there is more than one zero, all other elements will be zero
        if zero_count > 1:
            return [0] * len(nums)

        # If there is exactly one zero, the result will be zero for all elements except at the zero position
        if zero_count == 1:
            return [0 if num != 0 else prod for num in nums]

        # If there are no zeros, divide the product by each element to get the result
        res = [int(prod / num) for num in nums]
        return res