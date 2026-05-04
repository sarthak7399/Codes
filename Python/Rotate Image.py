# https://leetcode.com/problems/rotate-image/

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)  # Size of the square matrix

        # Step 1: Transpose the matrix
        # Convert rows into columns by swapping matrix[i][j] with matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):  # Only process upper triangle
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        # This completes 90° clockwise rotation
        for row in matrix:
            row.reverse()