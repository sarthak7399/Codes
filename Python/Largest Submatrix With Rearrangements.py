# https://leetcode.com/problems/largest-submatrix-with-rearrangements/

# Example 1:
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.

class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        
        # Dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Variable to store the maximum area found
        maxArea = 0
        
        # Array to store heights of consecutive 1s for each column
        # h[j] represents height of histogram at column j
        h = [0] * n

        # Traverse each row
        for i in range(m):

            # Build/update histogram heights
            for j in range(n):
                if matrix[i][j] == 1:
                    # Increase height if current cell is 1
                    h[j] += 1
                else:
                    # Reset height if current cell is 0
                    h[j] = 0

            # Sort heights in descending order
            # This simulates rearranging columns optimally
            sh = sorted(h, reverse=True)

            # Try forming rectangles using sorted heights
            for j in range(n):

                # If height is 0, no rectangle possible beyond this
                if sh[j] == 0:
                    break

                # Width = (j + 1), height = sh[j]
                # Area = height × width
                maxArea = max(maxArea, sh[j] * (j + 1))

        return maxArea