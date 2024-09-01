# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

# Example 1:
# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6

from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor_sum = 0  # Initialize the total XOR sum of all subsets
        
        # Iterate through all possible subsets using bitwise representation
        for subset_mask in range(1 << n):
            subset_xor = 0  # Initialize the XOR for the current subset
            
            for bit_position in range(n):
                # Check if the bit_position-th element is in the subset_mask-th subset
                if subset_mask & (1 << bit_position):
                    subset_xor ^= nums[bit_position]
            
            total_xor_sum += subset_xor  # Add the XOR of the current subset to the total sum
        
        return total_xor_sum  # Return the total XOR sum of all subsets
