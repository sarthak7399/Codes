# https://leetcode.com/problems/remove-methods-from-project/

# Example 1:
# Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]
# Output: [0,1,2,3]
# Explanation:
# Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.

from typing import List

class Solution:
    def remainingMethods( self, n: int, k: int, invocations: List[List[int]] ) -> List[int]:

        # Build a directed adjacency list where:
        # adj[src] contains all methods invoked by src.
        adj = {i: [] for i in range(n)}

        for src, dst in invocations:
            adj[src].append(dst)

        # Start traversal from the suspicious method k.
        q = [k]

        # Store all suspicious methods.
        # A method becomes suspicious if it is directly or
        # indirectly invoked by method k.
        visited = set([k])

        # Perform DFS using a list as a stack.
        while q:
            suspicious = q.pop()

            # Visit every method invoked by the
            # current suspicious method.
            for nei in adj[suspicious]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        # Store methods that can remain after removing
        # all suspicious methods.
        res = []

        for method in range(n):

            # Skip methods marked as suspicious.
            if method in visited:
                continue

            # Check whether a non-suspicious method invokes
            # a suspicious method.
            for nei in adj[method]:

                # If such an invocation exists, suspicious
                # methods cannot be removed safely.
                # Therefore, return all methods.
                if nei in visited:
                    return list(range(n))

            # This method is safe to keep.
            res.append(method)

        return res