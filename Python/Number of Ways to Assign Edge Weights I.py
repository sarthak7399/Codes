# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

# Example 1:
# Input: edges = [[1,2]]
# Output: 1
# Explanation:
# The path from Node 1 to Node 2 consists of one edge (1 → 2).
# Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

from collections import deque

class Solution:
    def assignEdgeWeights(self, edges):
        # Number of nodes in a tree with (n - 1) edges
        n = len(edges) + 1

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Stores maximum depth reached from root node 1
        mx_depth = 0

        # BFS queue: (node, depth)
        q = deque([(1, 0)])

        # Track visited nodes to avoid revisiting
        visited = [False] * (n + 1)

        # Perform BFS starting from node 1
        while q:
            node, depth = q.popleft()

            visited[node] = True

            # Update maximum depth encountered so far
            mx_depth = max(mx_depth, depth)

            # Visit all unvisited neighbors
            for child in adj[node]:
                if not visited[child]:
                    q.append((child, depth + 1))

        # Return 2^(max_depth - 1) modulo 1e9+7
        return pow(2, mx_depth - 1, 10**9 + 7)