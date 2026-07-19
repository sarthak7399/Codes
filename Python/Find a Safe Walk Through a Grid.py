# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

# Example 2:
# Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
# Output: false
# Explanation:
# A minimum of 4 health points is needed to reach the final cell safely.

from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # A large value representing an unreachable state
        INF = float('inf')

        # dist[i][j] = minimum health lost to reach cell (i, j)
        dist = [[INF] * n for _ in range(m)]

        # Deque used for 0-1 BFS
        dq = deque()

        # Starting cell contributes its own cost
        dist[0][0] = grid[0][0]
        dq.appendleft((0, 0))

        # Four possible movement directions
        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        # Perform 0-1 BFS
        while dq:
            x, y = dq.popleft()

            # If we reached the destination,
            # check whether remaining health is positive
            if x == m - 1 and y == n - 1:
                return dist[x][y] < health

            # Explore all neighboring cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check bounds
                if 0 <= nx < m and 0 <= ny < n:

                    # Cost of entering the next cell
                    w = grid[nx][ny]

                    # Relax the edge
                    if dist[x][y] + w < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + w

                        # For weight 0, process immediately
                        if w == 0:
                            dq.appendleft((nx, ny))
                        # For weight 1, process later
                        else:
                            dq.append((nx, ny))

        # If destination was never popped,
        # check the computed minimum cost
        return dist[m - 1][n - 1] < health