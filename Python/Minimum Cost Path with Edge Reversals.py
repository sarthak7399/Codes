# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

# Example 1:
# Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
# Output: 5
# Explanation:
# Use the path 0 → 1 (cost 3).
# At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
# Total cost is 3 + 2 = 5.

import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph
        # For each edge u -> v with weight w:
        # 1. Normal traversal: u -> v cost w
        # 2. Edge reversal: v -> u cost 2*w
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        # Dijkstra Initialization
        # Heap stores (cost, node) to sort by min cost
        pq = [(0, 0)]
        min_costs = [float('inf')] * n
        min_costs[0] = 0

        while pq:
            d, u = heapq.heappop(pq)

            # Early Exit: If we reached the target with the shortest path
            if u == n - 1:
                return d
            
            # Optimization: If current path is worse than already found, skip (Lazy Deletion)
            # In this implementation, the check before push handles most cases, 
            # but strictly speaking: if d > min_costs[u]: continue
            if d > min_costs[u]:
                continue

            for v, w in adj[u]:
                new_cost = d + w

                # Only push if we found a strictly better path
                if new_cost < min_costs[v]:
                    min_costs[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1