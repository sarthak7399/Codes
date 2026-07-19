# https://leetcode.com/problems/power-grid-maintenance/

# Example 1:
# Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
# Output: [3,2,3]
# Explanation:
# Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
# Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
# Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
# Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
# Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
# Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.

from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        This function processes queries on a network of 'c' computers.
        - Some computers are connected through given 'connections'.
        - Some computers may go offline or be queried.
        
        Queries:
            t == 1 → Query: Find the smallest online computer in the same connected component as x.
            t == 2 → Mark computer x as offline.
        
        Returns:
            List of answers for type 1 queries.
        """

        # -------------------------------------------
        # 🔹 Disjoint Set Union (Union-Find) structure
        # -------------------------------------------
        parent = list(range(c + 1))   # parent[i] = parent of node i
        size = [1] * (c + 1)          # size[i] = size of component rooted at i

        # Find with path compression
        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        # Union by size (attach smaller component to larger)
        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # -------------------------------------------
        # 🔹 Connect all computers based on connections
        # -------------------------------------------
        for u, v in connections:
            unite(u, v)

        # -------------------------------------------
        # 🔹 Create a min-heap for each connected component
        # -------------------------------------------
        heaps = {}   # {root_node: min-heap of all its members}
        for i in range(1, c + 1):
            r = find(i)
            if r not in heaps:
                heaps[r] = []
            heaps[r].append(i)
        for r in heaps:
            heapq.heapify(heaps[r])  # Convert list to min-heap for quick smallest-element access

        # -------------------------------------------
        # 🔹 Process each query
        # -------------------------------------------
        offline = [False] * (c + 1)  # Track whether a computer is offline
        ans = []                     # Store answers for type-1 queries

        for t, x in queries:
            if t == 2:
                # Type 2 → Mark computer as offline
                offline[x] = True
            else:
                # Type 1 → Find the smallest online computer in the same component
                if not offline[x]:
                    # If current computer is online, return it
                    ans.append(x)
                else:
                    # Otherwise, find its connected component’s root
                    r = find(x)
                    h = heaps.get(r, [])
                    # Remove all offline computers from heap top
                    while h and offline[h[0]]:
                        heapq.heappop(h)
                    # Append smallest online computer or -1 if none available
                    ans.append(h[0] if h else -1)

        # -------------------------------------------
        # 🔹 Return all results for type-1 queries
        # -------------------------------------------
        return ans
