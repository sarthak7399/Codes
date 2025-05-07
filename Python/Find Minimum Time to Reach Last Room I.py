# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

# Example 1:
# Input: moveTime = [[0,4],[4,4]]
# Output: 6
# Explanation:
# The minimum time required is 6 seconds.
# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in one second.

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)      # Number of rows in the grid
        m = len(moveTime[0])   # Number of columns in the grid

        # dist[r][c] holds the minimum time required to reach cell (r, c)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0  # Start at top-left corner (0,0) at time 0

        # Priority queue for Dijkstra's algorithm: (arrival_time, row, column)
        pq = [(0, 0, 0)]

        # 4 possible movement directions: right, left, down, up
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        while pq:
            t, r, c = heapq.heappop(pq)  # Get the earliest available cell
            if t > dist[r][c]:
                continue  # Skip if we already found a better time

            # If we reached the bottom-right corner, return the time
            if r == n - 1 and c == m - 1:
                return t

            # Explore all 4 adjacent neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    # Wait until neighbor cell becomes available (unlocks)
                    depart = max(t, moveTime[nr][nc])
                    arrive = depart + 1  # Takes 1 unit time to move
                    if arrive < dist[nr][nc]:
                        # Update best time to reach neighbor
                        dist[nr][nc] = arrive
                        heapq.heappush(pq, (arrive, nr, nc))  # Add to queue

        return -1  # If destination is unreachable (shouldn't happen per constraints)
