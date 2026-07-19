# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

# Example 1:
# Input: robots = [4], distance = [3], walls = [1,10]
# Output: 1
# Explanation:
# robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.
# Thus, the answer is 1.

from typing import List
import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        
        n = len(robots)

        # Combine robot position and distance → [position, distance]
        x = [[robots[i], distance[i]] for i in range(n)]

        # Sort robots by position and walls for binary search
        x.sort()
        walls.sort()

        # Add a dummy robot at the end to avoid index out-of-bound
        x.append([10**9, 0])

        # -------- Helper: count walls in range [l, r] --------
        def query(l, r):
            if l > r:
                return 0
            
            # Count walls using binary search
            # rightmost index - leftmost index
            return bisect.bisect_right(walls, r) - bisect.bisect_left(walls, l)

        # -------- DP definition --------
        # dp[i][0] → max walls destroyed till i-th robot if it shoots LEFT
        # dp[i][1] → max walls destroyed till i-th robot if it shoots RIGHT
        dp = [[0, 0] for _ in range(n)]

        # -------- Base case (first robot) --------

        # Shooting LEFT: covers [pos - dist, pos]
        dp[0][0] = query(x[0][0] - x[0][1], x[0][0])

        if n > 1:
            # Shooting RIGHT: ensure it doesn't overlap with next robot
            dp[0][1] = query(
                x[0][0],
                min(x[1][0] - 1, x[0][0] + x[0][1])
            )
        else:
            # Only one robot → no overlap concern
            dp[0][1] = query(x[0][0], x[0][0] + x[0][1])

        # -------- DP transitions --------
        for i in range(1, n):

            # -------- Case 1: Current robot shoots RIGHT --------
            # Take best of previous (LEFT or RIGHT) + current contribution
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + \
                       query(
                           x[i][0],
                           min(x[i + 1][0] - 1, x[i][0] + x[i][1])
                       )

            # -------- Case 2: Current robot shoots LEFT (no overlap) --------
            # Extend from previous LEFT
            dp[i][0] = dp[i - 1][0] + \
                       query(
                           max(x[i][0] - x[i][1], x[i - 1][0] + 1),
                           x[i][0]
                       )

            # -------- Case 3: Current robot shoots LEFT (overlap with previous RIGHT) --------
            # Handle overlap with previous robot's RIGHT shooting range

            # Current robot's LEFT shooting range
            leftStart = max(x[i][0] - x[i][1], x[i - 1][0] + 1)
            leftEnd = x[i][0]

            # Overlapping region with previous robot's RIGHT range
            overlapStart = leftStart
            overlapEnd = min(x[i - 1][0] + x[i - 1][1], x[i][0] - 1)

            # Subtract overlap to avoid double counting
            res = dp[i - 1][1] + \
                  query(leftStart, leftEnd) - \
                  query(overlapStart, overlapEnd)

            # Take maximum of both LEFT options
            dp[i][0] = max(dp[i][0], res)

        # Final answer → best of last robot shooting LEFT or RIGHT
        return max(dp[n - 1][0], dp[n - 1][1])