# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

# Example 1:
# Input: edges = [[1,2]], queries = [[1,1],[1,2]]
# Output: [0,1]
# Explanation:
# Query [1,1]: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0.
# Query [1,2]: The path from Node 1 to Node 2 consists of one edge (1 → 2). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

from typing import List
import numpy as np
import collections
import sys

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        # Number of nodes in the tree
        n = len(edges) + 1

        MOD = 10**9 + 7

        # Maximum power needed for binary lifting
        LOG_N = 18

        # ---------------------------------------------------------------------
        # 1. Build adjacency list
        # ---------------------------------------------------------------------
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # up[node][j] = 2^j-th ancestor of node
        up = [[0] * LOG_N for _ in range(n + 2)]

        # depth[node] = depth from root
        depth = [0] * (n + 2)

        # ---------------------------------------------------------------------
        # 2. BFS to compute parent and depth of each node
        # ---------------------------------------------------------------------

        # Queue stores:
        # (current_node, parent_node, depth)
        queue = collections.deque([(1, 0, 0)])

        visited = [False] * (n + 1)
        visited[1] = True

        while queue:

            node, parent, d = queue.popleft()

            depth[node] = d
            up[node][0] = parent

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node, d + 1))

        # ---------------------------------------------------------------------
        # 3. Build Binary Lifting Table
        # ---------------------------------------------------------------------
        # up[node][j] stores the 2^j-th ancestor
        for j in range(1, LOG_N):

            for i in range(1, n + 1):

                prev = up[i][j - 1]

                up[i][j] = (
                    up[prev][j - 1]
                    if prev != 0
                    else 0
                )

        # ---------------------------------------------------------------------
        # Convert data structures to NumPy arrays
        # for vectorized query processing
        # ---------------------------------------------------------------------
        depth_np = np.array(depth, dtype=np.int32)
        up_np = np.array(up, dtype=np.int32)
        queries_np = np.array(queries, dtype=np.int32)

        # Extract all query endpoints
        u = queries_np[:, 0]
        v = queries_np[:, 1]

        # Save originals for distance calculation later
        orig_u = u.copy()
        orig_v = v.copy()

        # ---------------------------------------------------------------------
        # Step A: Bring both nodes to the same depth
        # ---------------------------------------------------------------------

        # Ensure u is always deeper (or equal depth)
        swap_mask = depth_np[u] < depth_np[v]
        u[swap_mask], v[swap_mask] = v[swap_mask], u[swap_mask]

        # Depth difference
        diff = depth_np[u] - depth_np[v]

        # Lift u upward until depths match
        for j in range(LOG_N):

            jump_mask = ((diff >> j) & 1) == 1

            u[jump_mask] = up_np[
                u[jump_mask],
                j
            ]

        # ---------------------------------------------------------------------
        # Step B: Find Lowest Common Ancestor (LCA)
        # ---------------------------------------------------------------------

        # Lift both nodes together from highest power down
        for j in range(LOG_N - 1, -1, -1):

            jump_mask = (
                (u != v)
                &
                (up_np[u, j] != up_np[v, j])
            )

            u[jump_mask] = up_np[u[jump_mask], j]
            v[jump_mask] = up_np[v[jump_mask], j]

        # If already equal, that node is LCA
        lca = u.copy()

        # Otherwise parent is the LCA
        not_equal_mask = (u != v)

        lca[not_equal_mask] = up_np[
            u[not_equal_mask],
            0
        ]

        # ---------------------------------------------------------------------
        # Step C: Compute path lengths
        # ---------------------------------------------------------------------
        path_lengths = (
            depth_np[orig_u]
            + depth_np[orig_v]
            - 2 * depth_np[lca]
        )

        # ---------------------------------------------------------------------
        # Precompute powers of 2 modulo MOD
        # ---------------------------------------------------------------------
        pow2 = np.zeros(n + 2, dtype=np.int64)

        pow2[0] = 1

        for i in range(1, n + 2):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        # ---------------------------------------------------------------------
        # Answer queries
        # ---------------------------------------------------------------------
        # If path length = 0:
        #     answer = 0
        #
        # Else:
        #     answer = 2^(path_length - 1)
        #
        ans = np.where(
            path_lengths == 0,
            0,
            pow2[(path_lengths - 1).astype(np.int32)]
        )

        return ans.tolist()