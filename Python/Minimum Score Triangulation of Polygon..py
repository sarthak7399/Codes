# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

# Example 2:
# Input: values = [3,7,4,5]
# Output: 144
# Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
# The minimum score is 144.

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for _ in range(n)]  
        # dp[i][j] stores the minimum triangulation score between vertices i..j

        for l in range(3, n+1):  # l = length of sub-polygon (at least 3 to form a triangle)
            for i in range(n-l+1):  
                j = i + l - 1  # sub-polygon end index
                dp[i][j] = float('inf')  # initialize with infinity
                for k in range(i+1, j):  # try splitting polygon at vertex k
                    # cost = triangulate left + triangulate right + area of triangle (i, j, k)
                    dp[i][j] = min(dp[i][j],
                                dp[i][k] + dp[k][j] + values[i]*values[j]*values[k])
        return dp[0][n-1]  # min score for entire polygon



# Polygon vertices: v[0], v[1], ..., v[n-1]

# Dynamic Programming builds solution from smaller sub-polygons to bigger:

# Step 1: Triangles (length=3)
#    i---k---j   → score = v[i]*v[j]*v[k]

# Step 2: Sub-polygons (length=4,5,...)
#    Split at k
#    i-------j
#    | \     |
#    |   \   |
#    |     \ |
#    k chosen → dp[i][j] = min(dp[i][k] + dp[k][j] + cost of triangle i,k,j)

# Step 3: Final Result
#    dp[0][n-1] gives min triangulation score of full polygon