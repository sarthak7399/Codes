# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

# Example 1:
# Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
# Output: 5
# Explanation:
# The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

class Solution:
    # Directions for diagonal movement: bottom-right, bottom-left, top-left, top-right
    DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def lenOfVDiagonal(self, grid):
        m, n = len(grid), len(grid[0])

        # 3D memo table to store results:
        # memo[i][j][mask] = max path length starting from (i,j) with given mask
        # mask encodes direction + whether a turn is allowed
        memo = [[[0] * (1 << 3) for _ in range(n)] for _ in range(m)]

        ans = 0  # Store longest valid diagonal length

        # Loop through every cell in grid
        for i in range(m):
            for j in range(n):
                # We only start from cells with value 1
                if grid[i][j] != 1:
                    continue

                # Pre-calculate max possible steps in each direction from (i,j)
                maxs = [m - i, j + 1, i + 1, n - j]

                # Try all 4 diagonal directions
                for k in range(4):
                    if maxs[k] > ans:  # Only explore if possible length is promising
                        # Start DFS from (i,j) with direction k
                        # canTurn = 1 means we are allowed to turn once
                        # target = 2 (we alternate between 1 and 2 in path)
                        ans = max(ans, self.dfs(i, j, k, 1, 2, grid, memo) + 1)
        return ans

    def dfs(self, i, j, k, canTurn, target, grid, memo):
        m, n = len(grid), len(grid[0])

        # Move in current diagonal direction (k)
        i += self.DIRS[k][0]
        j += self.DIRS[k][1]

        # Stop if out of bounds or cell value does not match the expected target
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != target:
            return 0

        # Encode state into mask = (direction, canTurn flag)
        mask = (k << 1) | canTurn

        # If already computed, return stored value
        if memo[i][j][mask] > 0:
            return memo[i][j][mask]

        # Continue straight in same direction, flip target (alternate between 1 and 2)
        res = self.dfs(i, j, k, canTurn, 2 - target, grid, memo)

        # If turning is allowed, try to turn clockwise (k → (k+1)%4)
        if canTurn == 1:
            maxs = [m - i - 1, j, i, n - j - 1]
            nk = (k + 1) % 4
            if maxs[nk] > res:  # Only explore if new direction can potentially improve result
                res = max(res, self.dfs(i, j, nk, 0, 2 - target, grid, memo))

        # Store result (path length from this state) in memo
        memo[i][j][mask] = res + 1
        return memo[i][j][mask]
