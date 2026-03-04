# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

# Example 1:
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

class Solution:
    def numSpecial(self, mat):
        # Get matrix dimensions
        m, n = len(mat), len(mat[0])

        # row[i] will store number of 1s in row i
        row = [0] * m
        
        # col[j] will store number of 1s in column j
        col = [0] * n

        # Step 1: Count number of 1s in each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        # Step 2: Count special positions
        # A position (i, j) is special if:
        # 1. mat[i][j] == 1
        # 2. row[i] == 1  → only one 1 in that row
        # 3. col[j] == 1  → only one 1 in that column
        #
        # The generator expression returns True/False values.
        # True is treated as 1, False as 0 in sum().
        return sum(
            mat[i][j] == 1 and row[i] == 1 and col[j] == 1
            for i in range(m)
            for j in range(n)
        )