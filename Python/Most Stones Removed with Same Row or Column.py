# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

# Example 1:
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Dictionary to store the graph connections
        graph = {}

        # Build the graph
        for x, y in stones:
            if x not in graph:
                graph[x] = []
            if ~y not in graph:
                graph[~y] = []
            graph[x].append(~y)  # Connect x coordinate with y using bitwise NOT for unique identification
            graph[~y].append(x)  # Connect y coordinate back to x

        # Set to track visited nodes
        visited = set()

        def dfs(node):
            """Depth-first search to visit all connected nodes."""
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        # Counting the number of connected components
        components = 0
        for x, y in stones:
            if x not in visited:
                dfs(x)
                components += 1

        # The number of stones that can be removed is total stones minus the number of connected components
        return len(stones) - components
