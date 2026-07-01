# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

# Example 1:
# Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
# Output: 0
# Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

from collections import deque
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Four possible directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # dist[r][c] = minimum distance from cell (r, c)
        # to any thief
        dist = [[float('inf')] * n for _ in range(n)]

        # Queue for multi-source BFS
        q = deque()

        # ---------------------------------------------------
        # Step 1: Add all thief cells to the queue
        # ---------------------------------------------------
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0

        # ---------------------------------------------------
        # Step 2: Multi-source BFS
        # Compute the minimum distance of every cell
        # from the nearest thief
        # ---------------------------------------------------
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and dist[nr][nc] == float('inf')
                ):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # ---------------------------------------------------
        # Step 3: Modified Dijkstra / Maximum-Minimum Path
        #
        # We want a path from (0,0) to (n-1,n-1)
        # that maximizes:
        # min(distance to thief along the path)
        # ---------------------------------------------------

        # Max heap:
        # (-safeness, row, col)
        max_heap = [(-dist[0][0], 0, 0)]

        # Best safeness factor achieved for each cell
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = dist[0][0]

        while max_heap:
            d, r, c = heapq.heappop(max_heap)

            # Convert back from negative value
            d = -d

            # Reached destination
            if r == n - 1 and c == n - 1:
                return d

            # Try moving in all four directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:

                    # Safeness of the new path is the minimum
                    # safeness seen so far and the next cell's
                    # distance to the nearest thief
                    new_safe = min(d, dist[nr][nc])

                    # Update only if this path is better
                    if new_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = new_safe
                        heapq.heappush(
                            max_heap,
                            (-new_safe, nr, nc)
                        )

        # No valid path found (should not happen per constraints)
        return -1
    