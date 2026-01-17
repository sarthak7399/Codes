# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

# Example 1:
# Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
# Output: 1
# Explanation:
# A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        maxSquare = 0  # maximum possible square side

        # Check every pair of rectangles
        for i in range(n - 1):
            a, b = bottomLeft[i]
            c, d = topRight[i]

            for j in range(i + 1, n):
                aj, bj = bottomLeft[j]
                cj, dj = topRight[j]

                # Compute overlap width and height
                width = min(c, cj) - max(a, aj)
                height = min(d, dj) - max(b, bj)

                # If they overlap
                if width > 0 and height > 0:
                    # Largest square that can fit in the overlap
                    square = min(width, height)
                    maxSquare = max(maxSquare, square)

        return maxSquare * maxSquare
