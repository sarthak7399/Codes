# https://leetcode.com/problems/maximal-rectangle/

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

class Solution:
    def area(self, heights: List[int]) -> int:
        # Stack will store indices of histogram bars
        stack = []
        maxArea = 0
        n = len(heights)

        # We go till n+1 to flush the stack at the end using height = 0
        for i in range(n + 1):
            # For last index, use height 0 to process all remaining bars
            h = 0 if i == n else heights[i]

            # While current height is smaller than the height at stack top
            # it means rectangle with stack top as height must end here
            while stack and h < heights[stack[-1]]:
                # Pop the height index
                height = heights[stack.pop()]

                # If stack is empty, width is from 0 to i
                # Else width is between current index and new stack top
                width = i if not stack else i - stack[-1] - 1

                # Update maximum area
                maxArea = max(maxArea, height * width)

            # Push current index to stack
            stack.append(i)

        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Edge case: empty matrix
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        # hist[j] = height of histogram at column j till current row
        hist = [0] * n
        ans = 0

        # Build histogram row by row
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    hist[j] += 1   # increase height
                else:
                    hist[j] = 0    # reset height if '0'

            # For each row's histogram, compute largest rectangle area
            ans = max(ans, self.area(hist))

        return ans
