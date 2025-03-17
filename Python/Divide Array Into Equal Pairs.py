# https://leetcode.com/problems/divide-array-into-equal-pairs/

# Example 1:
# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation: 
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}  # Dictionary to count occurrences of each number
        
        # Count frequency of each number
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        # Check if all counts are even
        for count in counter.values():
            if count % 2 != 0:  # If any count is odd, return False
                return False
        
        return True  # All numbers appear in pairs
