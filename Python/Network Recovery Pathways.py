# https://leetcode.com/problems/network-recovery-pathways/

# Example 2:
# Input: edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12
# Output: 6
# Explanation:
# Node 3 is offline, so any path passing through 3 is invalid.
# Consider the remaining routes from 0 to 4:
# Path 0 → 1 → 4
# Total cost = 7 + 5 = 12 <= k, so this path is valid.
# The minimum edge‐cost along this path is min(7, 5) = 5.
# Path 0 → 2 → 3 → 4
# Node 3 is offline, so this path is invalid regardless of cost.
# Path 0 → 2 → 4
# Total cost = 6 + 6 = 12 <= k, so this path is valid.
# The minimum edge‐cost along this path is min(6, 6) = 6.
# Among the two valid paths, their scores are 5 and 6. Therefore, the answer is 6.

from cmath import inf
from collections import deque
from typing import List

class Solution:
    def check(self, mid, adj, topo, online, k, n):
        # dist[i] = minimum path cost to reach node i
        # using only edges with weight >= mid
        dist = [inf] * n
        dist[0] = 0

        # Process nodes in topological order since the graph is a DAG
        for u in topo:

            # Skip unreachable nodes
            if dist[u] == inf:
                continue

            # Intermediate nodes must be online
            # (source and destination are always allowed)
            if u != 0 and u != n - 1 and not online[u]:
                continue

            # Traverse outgoing edges
            for v, w in adj[u]:

                # We only consider edges whose weight
                # is at least the candidate score
                if w < mid:
                    continue

                # Destination node can always be visited,
                # but other intermediate nodes must be online
                if v != n - 1 and not online[v]:
                    continue

                # Relax the edge
                dist[v] = min(dist[v], dist[u] + w)

        # Check if we can reach node n-1
        # with total path cost at most k
        return dist[n - 1] <= k

    def findMaxPathScore(
        self,
        edges: List[List[int]],
        online: List[bool],
        k: int
    ) -> int:

        n = len(online)

        # Build adjacency list and indegree array
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        # Maximum edge weight (upper bound for binary search)
        max_edge = 0

        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1
            max_edge = max(max_edge, w)

        # -------------------------------------------------
        # Topological Sort (Kahn's Algorithm)
        # -------------------------------------------------
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in adj[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        # -------------------------------------------------
        # Binary search on the answer:
        # maximum possible minimum edge weight
        # -------------------------------------------------
        low, high = 0, max_edge
        ans = -1

        while low <= high:

            mid = (low + high) // 2

            # If a valid path exists with score >= mid,
            # try to increase the answer
            if self.check(mid, adj, topo, online, k, n):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans