# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

# Example 1:
# Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
# Output: 2
# Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
# It can be shown that we need to remove at least 2 obstacles, so we return 2.
# Note that there may be other ways to remove 2 obstacles to create a path.

import collections
from typing import List
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distance = [[float('inf')] * n for _ in range(m)]
        dq = collections.deque()

        distance[0][0] = 0
        dq.appendleft((0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while dq:
            x, y = dq.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    newDist = distance[x][y] + grid[nx][ny]
                    if newDist < distance[nx][ny]:
                        distance[nx][ny] = newDist
                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        return distance[m-1][n-1]