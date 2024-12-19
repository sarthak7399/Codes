# https://leetcode.com/problems/max-chunks-to-make-sorted/

# Example 1:
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize variables
        max_seen = 0
        chunks = 0

        # Iterate through the array
        for i, num in enumerate(arr):
            # Update the maximum value seen so far
            max_seen = max(max_seen, num)

            # If the maximum value seen so far equals the current index,
            # it means we can form a chunk up to this point.
            if max_seen == i:
                chunks += 1

        return chunks