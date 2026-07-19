# https://leetcode.com/problems/diagonal-traverse/

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Explanation: The diagonal traversal is: 1 -> 2 -> 4 -> 7 -> 5 -> 3 -> 6 -> 8 -> 9.

from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle empty matrix case
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])  # Number of rows and columns
        result = []  # Final traversal order
        row = col = 0  # Start position at top-left corner

        # Iterate through all elements (total m * n elements)
        for _ in range(m * n):
            result.append(matrix[row][col])  # Add current element

            # Check the direction of traversal:
            # If row + col is even → move "up-right"
            if (row + col) % 2 == 0:
                if col == n - 1:  # If at last column → move down
                    row += 1
                elif row == 0:  # If at first row → move right
                    col += 1
                else:  # Otherwise → move up-right
                    row -= 1
                    col += 1
            else:  
                # If row + col is odd → move "down-left"
                if row == m - 1:  # If at last row → move right
                    col += 1
                elif col == 0:  # If at first column → move down
                    row += 1
                else:  # Otherwise → move down-left
                    row += 1
                    col -= 1

        return result  # Return full diagonal traversal
