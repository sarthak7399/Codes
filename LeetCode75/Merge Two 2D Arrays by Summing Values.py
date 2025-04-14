# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

# Example 1:
# Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
# Output: [[1,6],[2,3],[3,2],[4,6]]
# Explanation: The resulting array contains the following:
# - id = 1, the value of this id is 2 + 4 = 6.
# - id = 2, the value of this id is 3.
# - id = 3, the value of this id is 2.
# - id = 4, the value of this id is 5 + 1 = 6.

from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Initialize pointers for both arrays
        i, j = 0, 0
        result = []
        
        # Traverse both arrays with two pointers
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 < id2:
                # Id1 is smaller, add it to result
                result.append([id1, val1])
                i += 1
            elif id2 < id1:
                # Id2 is smaller, add it to result
                result.append([id2, val2])
                j += 1
            else:
                # Ids are equal, sum the values
                result.append([id1, val1 + val2])
                i += 1
                j += 1
        
        # Add remaining elements from nums1, if any
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        
        # Add remaining elements from nums2, if any
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        
        return result