# https://leetcode.com/problems/flip-square-submatrix-vertically/

# Example 1:
# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3
# Output: [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]
# Explanation:
# The diagram above shows the grid before and after the transformation.

# translated using AI
class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        
        # We are reversing a k x k submatrix starting at (x, y)
        # The reversal is done vertically (top ↔ bottom rows)

        # Iterate only half the rows (like reversing an array)
        for i in range(k // 2):

            # Traverse all columns in the submatrix
            for j in range(k):

                # Swap elements:
                # Top row → (x + i)
                # Bottom row → (x + k - 1 - i)
                grid[x + i][y + j], grid[x + k - 1 - i][y + j] = \
                grid[x + k - 1 - i][y + j], grid[x + i][y + j]

        # Return modified grid
        return grid