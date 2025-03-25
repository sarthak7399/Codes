# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

# Example 1:
# Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
# Output: true
# Explanation:
# The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

from typing import List

class Solution:
    def isPossible(self, rectangles: List[List[int]], k: int) -> bool:
        # Sort rectangles based on the k-th coordinate (either x or y)
        rectangles.sort(key=lambda x: x[k])

        cuts = 0
        mx = rectangles[0][k + 2]  # Track the maximum endpoint

        # Iterate through rectangles to check for possible cuts
        for rect in rectangles:
            b, e = rect[k], rect[k + 2]

            # If there's a valid gap, increment the cut count
            if mx <= b:
                cuts += 1

            # Update the maximum endpoint
            mx = max(mx, e)

        # At least two valid cuts should be present
        return cuts >= 2

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return self.isPossible(rectangles, 0) or self.isPossible(rectangles, 1)