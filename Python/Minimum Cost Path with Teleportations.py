# https://leetcode.com/problems/minimum-cost-path-with-teleportations/

# Example 1:
# Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2
# Output: 7
# Explanation:
# Initially we are at (0, 0) and cost is 0.
# Current Position	Move	New Position	Total Cost
# (0, 0)	Move Down	(1, 0)	0 + 2 = 2
# (1, 0)	Move Right	(1, 1)	2 + 5 = 7
# (1, 1)	Teleport to (2, 2)	(2, 2)	7 + 0 = 7
# The minimum cost to reach bottom-right cell is 7.

from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        """
        suppose dp[i][j] yields the minimum cost to reach i, j
        then when k = 0, this is a dp problem where
        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        """
        m, n = len(grid), len(grid[0])
        # construct the teleportation order
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[grid[i][j]].append((i, j))
        
        # construct costs for k = 0
        inf = float('inf')
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 0
        def update():
            for i in range(m):
                for j in range(n):
                    temp = grid[i][j] + min(
                        dp[i-1][j] if i else inf, 
                        dp[i][j-1] if j else inf
                    )
                    if temp < dp[i][j]: dp[i][j] = temp
        update()

        # teleport k times
        keys = sorted(d, reverse=True)
        for _ in range(k):
            dist = inf
            for key in keys:
                for i, j in d[key]:
                    if dp[i][j] < dist: dist = dp[i][j]
                for i, j in d[key]:
                    dp[i][j] = dist
            update()
        return dp[-1][-1]