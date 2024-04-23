# https://leetcode.com/problems/minimum-height-trees/

# Example 1:
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

from collections import defaultdict, deque
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # If there is only one node, return it as the root
        
        # Initialize the adjacency list and degree of each node
        adjacency_list = defaultdict(list)  # Initialize adjacency list
        degree = [0] * n  # Initialize degree of each node
        for u, v in edges:
            adjacency_list[u].append(v)  # Add edge from u to v
            adjacency_list[v].append(u)  # Add edge from v to u
            degree[u] += 1  # Increment degree of u
            degree[v] += 1  # Increment degree of v
        
        # Initialize leaves queue
        leaves = deque([i for i in range(n) if degree[i] == 1])  # Find initial leaves
        
        # Trim leaves until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)  # Get the number of leaves at current level
            remaining_nodes -= leaves_count  # Decrease the remaining nodes
            for _ in range(leaves_count):
                leaf = leaves.popleft()  # Remove leaf from queue
                for neighbor in adjacency_list[leaf]:  # Update degree of neighbors
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:  # If neighbor becomes a leaf, add to queue
                        leaves.append(neighbor)
        
        return list(leaves)  # Return remaining leaves as roots of minimum height trees
