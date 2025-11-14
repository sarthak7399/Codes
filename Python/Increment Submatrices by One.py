# https://leetcode.com/problems/increment-submatrices-by-one/

# Example 1:
# Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
# Output: [[1,1,0],[1,2,1],[0,1,1]]
# Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
# - In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
# - In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # 2D difference array initialised with zeros
        diff = [[0] * n for _ in range(n)]

        # Apply range updates using difference array logic
        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2 + 1):
                diff[i][col1] += 1          # Start of increment range
                if col2 + 1 < n:
                    diff[i][col2 + 1] -= 1  # End of increment range

        # Convert difference array to final values using prefix sums row-wise
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        return diff
