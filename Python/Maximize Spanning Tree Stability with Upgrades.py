# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

# Example 1:
# Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1
# Output: 2
# Explanation:
# Edge [0,1] with strength = 2 must be included in the spanning tree.
# Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
# The resulting spanning tree includes these two edges with strengths 2 and 6.
# The minimum strength in the spanning tree is 2, which is the maximum possible stability.

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        
        # Union-Find parent array for DSU (Disjoint Set Union)
        parent = list(range(n))

        # Find function with path compression
        # It finds the root parent of node i
        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]  # Path compression
                i = parent[i]
            return i

        # Minimum stability (minimum edge weight used in final network)
        min_m = float('inf')

        # Initially all nodes are separate components
        comp_count = n

        # First process all mandatory edges (must == 1)
        for u, v, w, must in edges:
            if must == 1:
                ru = find(u)
                rv = find(v)

                # If both nodes already connected → cycle → invalid graph
                if ru == rv:
                    return -1

                # Union operation
                parent[ru] = rv
                comp_count -= 1

                # Track the minimum weight among mandatory edges
                if w < min_m:
                    min_m = w

        # List to store optional edges
        opt = []

        # Collect optional edges that connect different components
        for u, v, w, must in edges:
            if must == 0:
                ru = find(u)
                rv = find(v)

                if ru != rv:
                    # Pack data into a single integer for faster sorting
                    # weight (30 bits) | ru (17 bits) | rv (17 bits)
                    opt.append((w << 34) | (ru << 17) | rv)

        # If graph is already connected using mandatory edges
        if comp_count == 1:
            return int(min_m)

        # -------- Radix Sort for optional edges (based on weight) --------
        # Sorting packed integers using radix sort for efficiency
        if len(opt) > 1:
            temp = [0] * len(opt)

            # Process 8-bit chunks from bit 34 to 64
            for shift in range(34, 64, 8):

                count = [0] * 256

                # Counting occurrences
                for val in opt:
                    count[(val >> shift) & 0xFF] += 1

                # Prefix sum
                for i in range(1, 256):
                    count[i] += count[i - 1]

                # Build sorted array
                for i in range(len(opt) - 1, -1, -1):
                    val = opt[i]
                    idx = (val >> shift) & 0xFF
                    count[idx] -= 1
                    temp[count[idx]] = val

                # Swap arrays
                opt, temp = temp, opt

        # Store weights of edges used to connect components
        upg = []

        # Traverse edges from largest weight to smallest
        for i in range(len(opt) - 1, -1, -1):

            packed = opt[i]

            # Extract ru and rv from packed value
            ru = find((packed >> 17) & 0x1FFFF)
            rv = find(packed & 0x1FFFF)

            # If they belong to different components → connect them
            if ru != rv:
                parent[ru] = rv
                upg.append(packed >> 34)  # Extract weight
                comp_count -= 1

                # Stop when graph becomes connected
                if comp_count == 1:
                    break

        # If still disconnected → impossible
        if comp_count > 1:
            return -1

        # -------- Apply upgrades (k operations allowed) --------
        # Traverse selected edges
        for i in range(len(upg) - 1, -1, -1):

            if k > 0:
                k -= 1

                # Upgrade doubles the edge weight
                upgraded = upg[i] << 1

                # Update minimum stability
                if upgraded < min_m:
                    min_m = upgraded
            else:
                # No upgrade left
                if upg[i] < min_m:
                    min_m = upg[i]
                break

        return int(min_m)