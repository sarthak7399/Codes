# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

# Example 1:
# Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1
# Output: 3
# Explanation:
# The optimal valid path from node 0 to node 2 is as follows:
# Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
# The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.

import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build an adjacency list containing directed edges and their weights.
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        # Initialize all distances to infinity.
        # dist[u][cnt] stores the minimum distance to reach node u
        # with cnt consecutive nodes having the same label.
        INF = 10**9
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Start from node 0 with a consecutive label count of 1 and distance 0.
        # Priority queue stores (distance, node, consecutive_count).
        pq = [(0, 0, 1)]
        dist[0][1] = 0

        # Run Dijkstra's algorithm.
        while pq:
            # Extract the state with the smallest distance.
            d, u, cnt = heapq.heappop(pq)

            # Skip this state if a shorter path has already been found.
            if d > dist[u][cnt]:
                continue

            # Since Dijkstra processes states in increasing distance order,
            # reaching the destination gives the shortest valid path.
            if u == n - 1:
                return d

            # Explore all outgoing edges from the current node.
            for v, w in g[u]:
                # Extend the consecutive count if labels match;
                # otherwise, start a new consecutive sequence.
                ncnt = cnt + 1 if labels[u] == labels[v] else 1

                # Skip paths that exceed the allowed consecutive count.
                if ncnt > k:
                    continue

                # Relax the edge if a shorter distance is found for this state.
                if d + w < dist[v][ncnt]:
                    dist[v][ncnt] = d + w

                    # Add the updated state to the priority queue.
                    heapq.heappush(pq, (dist[v][ncnt], v, ncnt))

        # Return -1 if the destination cannot be reached under the constraint.
        return -1