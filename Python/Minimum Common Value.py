# https://leetcode.com/problems/minimum-common-value/

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_set = set(nums2)  # Convert nums2 to a set for faster lookup
        
        # Iterate through nums1
        for num in nums1:
            if num in nums2_set:
                return num  # Return the common element found
        
        # If no common element is found, return -1
        return -1