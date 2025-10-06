# https://leetcode.com/problems/swim-in-rising-water/

# Example 1:
# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (time, row, col)
        heapq.heapify(heap)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            t, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True

            # 🏁 Reached destination
            if r == n - 1 and c == n - 1:
                return t

            # 🌊 Explore 4 directions
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    nt = max(t, grid[nr][nc])
                    heapq.heappush(heap, (nt, nr, nc))
        return -1
