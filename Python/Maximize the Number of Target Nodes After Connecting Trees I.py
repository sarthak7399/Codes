# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

# Example 1:
# Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2
# Output: [9,7,9,8,8]
# Explanation:
# For i = 0, connect node 0 from the first tree to node 0 from the second tree.
# For i = 1, connect node 1 from the first tree to node 0 from the second tree.
# For i = 2, connect node 2 from the first tree to node 4 from the second tree.
# For i = 3, connect node 3 from the first tree to node 4 from the second tree.
# For i = 4, connect node 4 from the first tree to node 4 from the second tree.

from collections import deque

class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        # Helper function: performs BFS up to depth `k` starting from `start` node
        def bfs(start, adj, k):
            if k == 0:
                return 1  # Only the starting node can be reached if k == 0

            visited = set([start])  # Keep track of visited nodes to avoid cycles
            q = deque([start])      # Queue for BFS
            level = 0               # Current BFS level
            nodes_reached = 1       # Start with the start node

            # Perform BFS level by level until we reach depth k
            while q and level < k:
                for _ in range(len(q)):
                    node = q.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            nodes_reached += 1  # Count all unique reachable nodes
                level += 1

            return nodes_reached

        # Determine number of nodes in both graphs
        n = max(max(e) for e in edges1) + 1  # Max node index in edges1
        m = max(max(e) for e in edges2) + 1  # Max node index in edges2

        # Build adjacency lists for both graphs
        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # For each node in graph1, compute how many nodes can be reached within k steps
        path1 = [bfs(i, adj1, k) for i in range(n)]

        max_found = 0
        # For graph2, if k > 0, compute the maximum nodes reachable from any node in k-1 steps
        # (since one step is used to jump from graph1 to graph2)
        if k > 0:
            for i in range(m):
                max_found = max(max_found, bfs(i, adj2, k - 1))

        # The total for each node in graph1 is nodes_reached_in_graph1 + max_possible_from_graph2
        return [p + max_found for p in path1]