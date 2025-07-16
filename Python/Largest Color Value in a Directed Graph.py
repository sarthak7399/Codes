# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

# Example 1:
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

import collections
from functools import cache
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        hashmap = collections.defaultdict(list)
        
        # Build the graph and immediately return -1 if there's a self-loop (which is a cycle)
        for u, v in edges:
            if u == v:
                return -1  # Self-loop = cycle, invalid case
            hashmap[u].append(v)

        visited = set()  # To track the current path for cycle detection

        @cache  # Memoization to avoid recomputation for the same (node, target_color)
        def dfs(curr, target):
            result = 0  # Max count of nodes with target color in the path starting at `curr`
            
            for adj in hashmap[curr]:
                if adj in visited:
                    return float('inf')  # Cycle detected
                visited.add(adj)
                result = max(result, dfs(adj, target))  # Recurse for next nodes
                visited.remove(adj)

            # If current node has the target color, add 1
            return result + 1 if colors[curr] == target else result

        max_path_value = 0  # Result to keep track of maximum color value along any path

        # Try every node and every color as starting condition
        for i in range(len(colors)):
            max_path_value = max(max_path_value, dfs(i, colors[i]))

        # If a cycle was detected in any path, return -1
        return -1 if max_path_value == float('inf') else max_path_value
