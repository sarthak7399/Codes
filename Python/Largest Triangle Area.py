# https://leetcode.com/problems/largest-triangle-area/

# Example 1:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        n = len(points)

        # Iterate over all combinations of 3 points
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    # Compute area using shoelace formula
                    current_area = abs(
                        0.5 * (x1 * (y2 - y3) +
                               x2 * (y3 - y1) +
                               x3 * (y1 - y2))
                    )

                    # Track maximum area
                    max_area = max(max_area, current_area)
                    
        return max_area
