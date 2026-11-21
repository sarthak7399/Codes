# https://leetcode.com/problems/find-subtree-sizes-after-changes/

# Example 1:
# Input: parent = [-1,0,0,1,1,1], s = "abaabc"
# Output: [6,3,1,1,1,1]
# Explanation:
# The parent of node 3 will change from node 1 to node 0.

from typing import List

class Solution:
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
        n = len(p)

        # adj stores the original tree structure
        adj = [[] for _ in range(n)]

        # tree stores the modified tree structure
        tree = [[] for _ in range(n)]

        # Stores the final subtree size for each node
        ans = [0] * n

        # last[c] stores the most recently visited ancestor
        # having character c (-1 means no such ancestor exists)
        last = [-1] * 26

        # Build the original tree using the parent array
        for i in range(1, n):
            adj[p[i]].append(i)

        def dfs(u):
            # Convert the current node's character into an index (0-25)
            c = ord(s[u]) - ord('a')

            # Save the previous occurrence of this character
            old = last[c]

            # If an ancestor with the same character exists,
            # update the current node's parent to that ancestor
            if u and old != -1:
                p[u] = old

            # Mark the current node as the latest occurrence of this character
            last[c] = u

            # Traverse all children in the original tree
            for v in adj[u]:
                dfs(v)

            # Restore the previous occurrence while backtracking
            # This ensures sibling branches are processed independently
            last[c] = old

        def calc(u):
            # Every node contributes 1 to its own subtree size
            ans[u] = 1

            # Recursively calculate and add the sizes of all child subtrees
            for v in tree[u]:
                ans[u] += calc(v)

            # Return the total subtree size of the current node
            return ans[u]

        # Perform DFS to update parent relationships
        # based on the nearest ancestor with the same character
        dfs(0)

        # Build the modified tree using the updated parent array
        for i in range(1, n):
            tree[p[i]].append(i)

        # Calculate subtree sizes in the modified tree
        calc(0)

        # Return the subtree size of every node
        return ans