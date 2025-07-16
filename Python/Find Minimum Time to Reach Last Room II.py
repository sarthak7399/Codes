# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

# Example 1:
# Input: moveTime = [[0,4],[4,4]]
# Output: 7
# Explanation:
# The minimum time required is 7 seconds.
# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.

from typing import List

class Solution:
    def minTimeToReach(self, t: List[List[int]]) -> int:
        n, m = len(t), len(t[0])  # Dimensions of the grid

        # 3D DP array to track minimum time to reach (x, y) with a certain parity (0 or 1)
        # dp[x][y][0] - arriving at cell (x,y) with even number of moves
        # dp[x][y][1] - arriving at cell (x,y) with odd number of moves
        dp = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0  # Starting at (0,0) at time 0 with parity 0 (even)

        from heapq import heappush, heappop
        pq = [(0, 0, 0, 0)]  # Priority queue with (time, x, y, parity)

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            time, x, y, parity = heappop(pq)

            # If we already found a better time for this state, skip
            if dp[x][y][parity] < time:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Skip if out of bounds
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                # You must wait until the target cell's unlock time (t[nx][ny])
                # You also need to add 1 extra unit of time based on your current parity
                wait_time = max(time, t[nx][ny])
                next_parity = 1 - parity
                next_time = wait_time + 1 + parity  # 1 + parity handles alternating move delays

                # If reaching bottom-right corner, return immediately
                if nx == n - 1 and ny == m - 1:
                    return next_time

                # Only proceed if this path gives a better time
                if next_time < dp[nx][ny][next_parity]:
                    dp[nx][ny][next_parity] = next_time
                    heappush(pq, (next_time, nx, ny, next_parity))

        return -1  # If destination is unreachable (per constraints, should not happen)
