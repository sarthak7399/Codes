# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

# Example 1:
# Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# Output: 5
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
# It can be shown that no other path has less score.

from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build the adjacency list:
        # adj[u] = [(neighbor, distance), ...]
        adj = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Visited array for BFS
        vis = [False] * (n + 1)

        # Start BFS from city 1
        q = deque([1])
        vis[1] = True

        # Stores the minimum road distance
        # in the connected component containing city 1
        ans = float('inf')

        while q:

            node = q.popleft()

            # Explore all neighboring roads
            for nei, wt in adj[node]:

                # Update the minimum road distance seen so far
                ans = min(ans, wt)

                # Visit the neighbor if not already visited
                if not vis[nei]:
                    vis[nei] = True
                    q.append(nei)

        return ans