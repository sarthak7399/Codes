# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

# Example 1:
# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
# - [3]
# - [3,1]

from typing import List

class Solution:
    def backtrack(self, nums, index, currentOR, maxOR, count):
        # If current OR equals the maximum possible OR, we found a valid subset
        if currentOR == maxOR:
            count[0] += 1
        
        # Explore all possible subsets by including each element starting from index
        for i in range(index, len(nums)):
            # Include nums[i] and move to the next index
            self.backtrack(nums, i + 1, currentOR | nums[i], maxOR, count)
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        
        # Step 1: Compute the maximum possible OR of all elements combined
        for num in nums:
            maxOR |= num
        
        count = [0]  # Use a list to hold count so it can be updated inside backtrack
        
        # Step 2: Use backtracking to count how many subsets have OR equal to maxOR
        self.backtrack(nums, 0, 0, maxOR, count)
        
        return count[0]