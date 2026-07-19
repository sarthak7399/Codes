# https://leetcode.com/problems/detect-cycles-in-2d-grid/

# Example 1:
# Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true

from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])  # Grid dimensions

        # Visited matrix to track explored cells
        visited = [[False] * n for _ in range(m)]

        # Possible 4-directional moves (down, up, right, left)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Traverse every cell in the grid
        for r in range(m):
            for c in range(n):
                # Skip if already visited
                if visited[r][c]:
                    continue

                # Stack for DFS: (current_row, current_col, parent_row, parent_col)
                stack = [(r, c, -1, -1)]

                # Mark starting cell as visited
                visited[r][c] = True

                # Perform DFS
                while stack:
                    cr, cc, pr, pc = stack.pop()

                    # Explore all 4 directions
                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc

                        # Skip out-of-bounds cells
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            continue

                        # Only move to cells with same character
                        if grid[nr][nc] != grid[cr][cc]:
                            continue

                        # Skip the parent cell (to avoid trivial backtracking)
                        if nr == pr and nc == pc:
                            continue

                        # If already visited and not parent → cycle detected
                        if visited[nr][nc]:
                            return True

                        # Mark as visited and continue DFS
                        visited[nr][nc] = True
                        stack.append((nr, nc, cr, cc))

        # No cycle found in any component
        return False