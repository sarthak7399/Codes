# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

# Example 1:
# Input: nums = [2,1,3,4,5,2]
# Output: 7
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
# - 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
# - 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
# Our score is 1 + 2 + 4 = 7.

from typing import List
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        
        # A list to track whether an element is marked
        marked = [False] * n
        
        # Sort the original list based on values, maintaining indices
        sorted_indices = sorted(range(n), key=lambda x: nums[x])
        
        for i in sorted_indices:
            if not marked[i]:
                score += nums[i]
                # Mark the current element and its neighbors
                marked[i] = True
                if i > 0:  # Mark the left neighbor
                    marked[i - 1] = True
                if i < n - 1:  # Mark the right neighbor
                    marked[i + 1] = True
        
        return score