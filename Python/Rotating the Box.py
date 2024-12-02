# https://leetcode.com/problems/rotating-the-box/

# Example 1:
# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]

from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Get the dimensions of the input box
        ROWS, COLS = len(box), len(box[0])

        # Initialize the result matrix (rotated version of the box) with empty cells ('.')
        # After rotation, the number of rows in the result will be the number of columns in the input
        # and vice versa.
        res = [["."] * ROWS for _ in range(COLS)]

        # Process each row of the box
        for r in range(ROWS):
            # `i` is the position to place the next stone ('#') in the rotated box
            # Start from the last column of the current row in the result matrix
            i = COLS - 1
            
            # Traverse the current row from right to left
            for c in reversed(range(COLS)):
                if box[r][c] == "#":  
                    # If the current cell has a stone ('#'), place it in the appropriate position in `res`
                    res[i][ROWS - r - 1] = "#"
                    # Move the pointer `i` one position left in the rotated row
                    i -= 1
                elif box[r][c] == "*":  
                    # If the current cell has an obstacle ('*'), place it in the rotated matrix
                    res[c][ROWS - r - 1] = "*"
                    # Reset the stone placement pointer `i` to the left of the obstacle
                    i = c - 1

        # Return the rotated box
        return res
