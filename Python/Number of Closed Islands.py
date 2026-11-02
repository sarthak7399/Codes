# https://leetcode.com/problems/number-of-closed-islands/

# Example 1:
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        # Get the number of rows and columns in the grid.
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # Stop if the cell is out of bounds or is not land (0).
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1:
                return

            # Mark the visited land cell as water (1) to avoid revisiting it.
            grid[i][j] = 1

            # Explore all four adjacent directions.
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Remove all land connected to the left and right boundaries.
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n - 1] == 0:
                dfs(i, n - 1)

        # Remove all land connected to the top and bottom boundaries.
        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m - 1][j] == 0:
                dfs(m - 1, j)

        # Count the remaining land regions, which are closed islands.
        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    # Found a closed island; count it and mark its cells visited.
                    ans += 1
                    dfs(i, j)

        # Return the total number of closed islands.
        return ans