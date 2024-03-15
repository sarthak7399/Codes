# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-03-15

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Calculate the difference between the sum of all elements in nums and the sum of all unique elements in nums
        # This difference represents the total sum contributed by duplicate elements in nums
        duplicate_sum = sum(nums) - sum(set(nums))
        
        # Calculate the difference between the sum of natural numbers from 1 to len(nums) and the sum of all unique elements in nums
        # This difference represents the sum of all missing elements in nums
        missing_sum = len(nums) * (len(nums) + 1) // 2 - sum(set(nums))
        
        # Return both the duplicate sum and missing sum as a list
        return [duplicate_sum, missing_sum]