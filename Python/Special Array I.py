# https://leetcode.com/problems/special-array-i/

# Example 1:
# Input: nums = [1]
# Output: true
# Explanation:
# There is only one element. So the answer is true.

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        Checks if an array is 'special', meaning adjacent elements have alternating parity.
        
        Args:
        nums (List[int]): The input list of integers.
        
        Returns:
        bool: True if the array is special, False otherwise.
        """

        n = len(nums)
        
        # If there's only one element, it's automatically special
        if n == 1:
            return True

        # Iterate through the array and check if adjacent elements have the same parity
        for i in range(n - 1):
            # If two adjacent numbers are both even or both odd, return False
            if nums[i] % 2 == nums[i + 1] % 2:
                return False

        # If all adjacent pairs have alternating parity, return True
        return True
