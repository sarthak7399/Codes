# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:    # Calculate the XOR of all elements
            xor ^= num      # XOR each element with the result of the previous XOR
        return xor