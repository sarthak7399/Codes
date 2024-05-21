# https://leetcode.com/problems/subsets/

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Get the length of the input list
        length_of_nums = len(nums)
        
        # Initialize the result list to store all subsets
        all_subsets = []
        
        # Iterate over the range from 0 to 2^n (exclusive), where n is the length of nums
        for subset_mask in range(1 << length_of_nums):  # 1 << n is 2^n
            current_subset = []
            
            # Iterate over each bit position
            for bit_position in range(length_of_nums):
                # Check if the bit at position 'bit_position' is set in 'subset_mask'
                if subset_mask & (1 << bit_position):
                    # If set, include the corresponding element from nums in the current subset
                    current_subset.append(nums[bit_position])
            
            # Add the current subset to the list of all subsets
            all_subsets.append(current_subset)
        
        # Return the list of all subsets
        return all_subsets
