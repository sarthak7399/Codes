# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

# Example 1:
# Input: grid = [[2,4,3],[6,5,2]]
# Output: true
# Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        # Mapping of each street type to the directions it supports
        # Directions are encoded as:
        # 0 → left, 1 → right, 2 → up, 3 → down
        dirs = {
            1: {0, 1},  # left ↔ right
            2: {2, 3},  # up ↔ down
            3: {0, 3},  # left ↔ down
            4: {1, 3},  # right ↔ down
            5: {0, 2},  # left ↔ up
            6: {1, 2},  # right ↔ up
        }

        # Possible moves:
        # (delta_row, delta_col, current_cell_direction, next_cell_direction)
        moves = [
            (0, -1, 0, 1),   # move left → current needs left, next needs right
            (0, 1, 1, 0),    # move right → current needs right, next needs left
            (-1, 0, 2, 3),   # move up → current needs up, next needs down
            (1, 0, 3, 2),    # move down → current needs down, next needs up
        ]

        rows = len(grid)
        cols = len(grid[0])

        # Track visited cells to avoid cycles
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True

        # BFS queue starting from top-left cell
        queue = deque([(0, 0)])
 
        # Perform BFS
        while queue:
            row, col = queue.popleft()

            # If we reach bottom-right cell → valid path exists
            if row == rows - 1 and col == cols - 1:
                return True

            # Try all possible directions
            for dr, dc, dx, dy in moves:
                nr = row + dr
                nc = col + dc

                # Check bounds, visited status, and valid street connections
                if (0 <= nr < rows and 0 <= nc < cols
                        and not visited[nr][nc]
                        # Current cell must allow movement in direction dx
                        and dx in dirs[grid[row][col]]
                        # Next cell must allow entry from direction dy
                        and dy in dirs[grid[nr][nc]]):

                    visited[nr][nc] = True
                    queue.append((nr, nc))

        # If BFS completes without reaching destination
        return False