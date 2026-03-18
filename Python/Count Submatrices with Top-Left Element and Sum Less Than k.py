# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

# Example 1:
# Input: grid = [[7,6,3],[6,6,1]], k = 18
# Output: 4
# Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.

class Solution:
    def countSubmatrices(self, grid, k):
        
        # Number of rows and columns
        m = len(grid)
        n = len(grid[0])
        
        # Final answer: count of valid submatrices
        ans = 0

        # -------- Step 1: Column-wise prefix sum --------
        # Convert grid so that each cell contains sum of elements
        # from row 0 to current row (same column)
        for i in range(1, m):
            for j in range(n):
                grid[i][j] += grid[i - 1][j]

        # -------- Step 2: Count valid subarrays per row --------
        # Each row now represents sum of submatrix from row 0 → i
        for i in range(m):

            # Running sum across columns
            s = 0

            for j in range(n):

                # Add current column value
                s += grid[i][j]

                # If sum exceeds k, no need to continue further
                # (since adding more columns will only increase sum)
                if s > k:
                    break

                # Valid submatrix found
                # (top-left at (0,0) and bottom-right at (i,j))
                ans += 1

        return ans