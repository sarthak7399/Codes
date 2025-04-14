# https://leetcode.com/problems/count-the-number-of-complete-components/

# Example 1:
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.

from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list representation of the graph
        G = [[] for i in range(n)]
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        
        seen = [0] * n  # Track visited nodes
        res = 0  # Count of complete components

        for i in range(n):
            if seen[i]:  # Skip already visited nodes
                continue
            
            bfs = [i]  # Start BFS from node i
            seen[i] = 1
            
            # Perform BFS to explore the component
            for j in bfs:
                for k in G[j]:
                    if seen[k] == 0:
                        bfs.append(k)
                        seen[k] = 1
            
            # Check if the component forms a complete subgraph
            if all(len(G[j]) == len(bfs) - 1 for j in bfs):
                res += 1  # Increment count if complete
        
        return res

