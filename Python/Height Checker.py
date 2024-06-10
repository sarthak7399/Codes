# https://leetcode.com/problems/height-checker/

# Example 1:
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Step 1: Create the expected array by sorting the heights array
        expected = sorted(heights)
        
        # Step 2: Count the mismatches between heights and expected
        mismatch_count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1
                
        return mismatch_count