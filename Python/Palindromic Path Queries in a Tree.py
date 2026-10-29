# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]
# Output: [true,false]
# Explanation:
# "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
# "update 1 b": Update node 1 to 'b', now s = "abc".
# "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
# Thus, answer = [true, false].

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Build an adjacency list to represent the tree.
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # LOG determines the number of levels used for binary lifting to find LCA.
        LOG = 16
        up = [[-1] * n for _ in range(LOG)]  # up[k][u] stores the 2^k-th ancestor of node u.
        depth = [0] * n                      # Distance of each node from the root.
        inn = [0] * n                        # Entry time of each node in DFS.
        out = [0] * n                         # Exit time of each node in DFS.
        parent = [-1] * n                    # Immediate parent of each node.

        # Represent each character as a bit in a bitmask (a-z -> bits 0-25).
        mask = [1 << (ord(c) - 97) for c in s]
        timer = [1]  # Mutable counter for assigning DFS entry and exit times.

        def dfs(u, p):
            # Assign an entry time to this node.
            inn[u] = timer[0]
            timer[0] += 1

            # Store the parent and the immediate ancestor.
            parent[u] = p
            up[0][u] = p

            # Precompute ancestors at powers of two for binary lifting.
            for k in range(1, LOG):
                if up[k - 1][u] != -1:
                    up[k][u] = up[k - 1][up[k - 1][u]]

            # Visit all children of the current node.
            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

            # Record the exit time after processing the entire subtree.
            out[u] = timer[0]

        # Root the tree at node 0 and compute DFS and ancestor information.
        dfs(0, -1)

        # Fenwick tree supporting range XOR updates and prefix XOR queries.
        bit = [0] * (n + 2)

        def upd(i, val):
            # Apply a point XOR update in the Fenwick tree.
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def qry(i):
            # Compute the prefix XOR up to index i.
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def range_xor(l, r, val):
            # Apply XOR val to every position in the inclusive range [l, r].
            if l > r:
                return
            upd(l, val)
            upd(r + 1, val)

        # Initialize the Fenwick tree with each node's character bitmask.
        # A node's subtree occupies the DFS interval [inn[i], out[i] - 1].
        for i in range(n):
            range_xor(inn[i], out[i] - 1, mask[i])

        def get_lca(u, v):
            # Make u the deeper node so both nodes can be brought to the same depth.
            if depth[u] < depth[v]:
                u, v = v, u

            # Lift u upward until u and v have equal depths.
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = up[k][u]

            # If the nodes now match, that node is their LCA.
            if u == v:
                return u

            # Lift both nodes upward, starting from the largest jump,
            # while keeping them below their lowest common ancestor.
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            # Their parent is the lowest common ancestor.
            return parent[u]

        def path_xor(u, v):
            # Find the lowest common ancestor of u and v.
            l = get_lca(u, v)

            # Combine the root-to-node XOR values and the LCA's character.
            # This gives the XOR mask of characters along the path from u to v.
            return qry(inn[u]) ^ qry(inn[v]) ^ mask[l]

        ans = []

        # Process each query.
        for q in queries:
            if q[0] == 'u':
                # Parse the node index from the update query string.
                u = 0
                i = 7
                while q[i] != ' ':
                    u = u * 10 + (ord(q[i]) - 48)
                    i += 1

                # Convert the new character into its bitmask.
                c = q[-1]
                nm = 1 << (ord(c) - 97)

                # XOR delta represents the bits that change between old and new characters.
                delta = mask[u] ^ nm
                mask[u] = nm

                # Update the XOR contribution of this node across its entire subtree.
                range_xor(inn[u], out[u] - 1, delta)

            else:
                # Parse the two node indices from the path query string.
                u = 0
                v = 0
                i = 6

                # Read the first node index.
                while q[i] != ' ':
                    u = u * 10 + (ord(q[i]) - 48)
                    i += 1

                # Skip the space between the two node indices.
                i += 1

                # Read the second node index.
                while i < len(q):
                    v = v * 10 + (ord(q[i]) - 48)
                    i += 1

                # Get the character bitmask along the path from u to v.
                m = path_xor(u, v)

                # A palindrome can be formed if at most one character
                # occurs an odd number of times, represented by at most one set bit.
                ans.append(bin(m).count('1') <= 1)

        # Return the results of all path queries.
        return ans