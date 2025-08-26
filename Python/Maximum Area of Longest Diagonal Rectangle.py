# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

# Example 1:
# Input: dimensions = [[9,3],[8,6]]
# Output: 48
# Explanation: 
# For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈ 9.487.
# For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
# So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.

class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        # Initialize variables to track maximum diagonal length (squared) and area
        max_area, max_diag = 0, 0

        # Iterate over each rectangle given as [length, width]
        for l, w in dimensions:
            # Calculate diagonal length squared (Pythagoras theorem, without sqrt for efficiency)
            curr_diag = l * l + w * w

            # Update if:
            # 1. Current diagonal is longer than the max diagonal seen so far, OR
            # 2. Diagonal is equal but area is larger
            if curr_diag > max_diag or (curr_diag == max_diag and l * w > max_area):
                max_diag = curr_diag   # Update max diagonal (squared)
                max_area = l * w       # Update max area

        # Return the area of the rectangle with the maximum diagonal (or largest area if tie)
        return max_area
