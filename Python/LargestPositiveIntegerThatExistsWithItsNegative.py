# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

# Example 1:
# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.

# Example 2:
# Input: nums = [-1,10,6,7,-7,1]
# Output: 7
# Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # Sort the given list of numbers
        nums.sort()
        n = len(nums)
        
        # Iterate through the list in reverse order
        for i in range(n-1, -1, -1):
            # Check if the current number is positive and its negation exists in the list
            if nums[i] > 0 and -nums[i] in nums:
                # If such a pair exists, return the current number
                return nums[i]
        
        # If no such pair found, return -1
        return -1