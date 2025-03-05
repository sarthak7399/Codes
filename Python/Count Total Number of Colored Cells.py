# https://leetcode.com/problems/count-total-number-of-colored-cells/

# Example 1:
# Input: n = 1
# Output: 1
# Explanation: After 1 minute, there is only 1 blue cell, so we return 1.

class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1  # Starting with the center cell

        i = 0
        while i < n:
            res = res + (4 * i)  # Each layer adds 4 * i new cells
            i += 1  # Move to the next layer
            
        return res  # Return the total number of colored cells
