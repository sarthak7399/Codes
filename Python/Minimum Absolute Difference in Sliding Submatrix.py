# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

# Example 1:
# Input: grid = [[1,8],[3,-2]], k = 2
# Output: [[2]]
# Explanation:
# There is only one possible k x k submatrix: [[1, 8], [3, -2]].
# Distinct values in the submatrix are [1, 8, 3, -2].
# The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].

class Solution:
    def minAbsDiff(self, grid, k):
        
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Result matrix of size (m-k+1) x (n-k+1)
        # Each cell represents a k x k subgrid
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        # Iterate over all possible top-left corners of k x k subgrids
        for i in range(m - k + 1):
            for j in range(n - k + 1):

                # Temporary list to store elements of current k x k subgrid
                temp = []

                # Collect all elements inside the k x k subgrid
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        temp.append(grid[x][y])

                # If subgrid size is 1x1 → no pair exists
                if k == 1:
                    ans[i][j] = 0
                    continue

                # Remove duplicates and sort the elements
                temp = sorted(set(temp))

                # If only one unique element → min difference is 0
                if len(temp) <= 1:
                    ans[i][j] = 0
                    continue

                # Find minimum absolute difference between consecutive elements
                mini = float('inf')
                for p in range(1, len(temp)):
                    mini = min(mini, abs(temp[p] - temp[p - 1]))

                # Store result
                ans[i][j] = mini

        return ans