# https://leetcode.com/problems/apply-operations-to-an-array/

# Example 1:
# Input: nums = [1,2,2,1,1,0]
# Output: [1,4,2,0,0,0]
# Explanation: We do the following operations:
# - i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
# - i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change nums[2] to 0. The array becomes [1,4,0,1,1,0].
# - i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
# - i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change nums[4] to 0. The array becomes [1,4,0,2,0,0].
# - i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change nums[5] to 0. The array becomes [1,4,0,2,0,0].
# After that, we shift the 0's to the end, which gives the array [1,4,2,0,0,0].

from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        Applies operations to an array as follows:

        - If the current element is equal to the next element, double the current element and set the next element to 0.
        - Shift all 0's to the end of the array.

        Args:
            nums (List[int]): The array to be modified.

        Returns:
            List[int]: The modified array.
        """
        
        n = len(nums)
        
        # Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Shift zeros to the end (in-place)
        non_zero_idx = 0
        
        # Move all non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1
        
        # Fill the remaining positions with zeros
        for i in range(non_zero_idx, n):
            nums[i] = 0
        
        return nums
        