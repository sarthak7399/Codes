# https://leetcode.com/problems/set-matrix-zeroes/

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the input matrix in-place such that if an element is 0,
        its entire row and column are set to 0.
        """

        n, m = len(matrix), len(matrix[0])  # Get dimensions of the matrix

        # Use bitmasks to track rows and columns that need to be zeroed
        col0, row0 = 0, 0

        # Step 1: Identify rows and columns that contain at least one zero
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == 0:
                    # Set the i-th bit in row0 to mark row i
                    row0 |= (1 << i)
                    # Set the j-th bit in col0 to mark column j
                    col0 |= (1 << j)

        # Step 2: Zero out marked rows
        for i in range(n):
            if (row0 >> i) & 1:  # Check if i-th bit is set
                for j in range(m):
                    matrix[i][j] = 0  # Set entire row to zero

        # Step 3: Zero out marked columns
        for j in range(m):
            if (col0 >> j) & 1:  # Check if j-th bit is set
                for i in range(n):
                    matrix[i][j] = 0  # Set entire column to zero
