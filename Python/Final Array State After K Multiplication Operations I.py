# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

# Example 1:
# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
# Output: [8,4,6,5,6]
# Explanation:
# Operation	Result
# After operation 1	[2, 2, 3, 5, 6]
# After operation 2	[4, 2, 3, 5, 6]
# After operation 3	[4, 4, 3, 5, 6]
# After operation 4	[4, 4, 6, 5, 6]
# After operation 5	[8, 4, 6, 5, 6]

from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Update the list `nums` by multiplying the smallest element by `multiplier` exactly `k` times.
        
        Args:
        nums (List[int]): The input list of integers.
        k (int): The number of operations to perform.
        multiplier (int): The value by which the smallest element is multiplied.

        Returns:
        List[int]: The final state of the list after `k` operations.
        """
        for _ in range(k):
            # Find the index of the smallest element in the list
            min_index = nums.index(min(nums))
            
            # Multiply the smallest element by the given multiplier
            nums[min_index] *= multiplier
        
        return nums
