# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

# Example 1:
# Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]
# Output: [1,-1]
# Explanation:
# To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).
# In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

from typing import List
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))  # Union-Find parent array
        min_path_cost = [-1] * n  # Stores the minimum cost for each connected component
        
        # Find operation with path compression
        def find_root(node: int) -> int:
            if parent[node] != node:
                parent[node] = find_root(parent[node])
            return parent[node]
        
        # Union operation: Connect nodes and update min_path_cost
        for source, target, weight in edges:
            source_root = find_root(source)
            target_root = find_root(target)
            
            # Update min path cost using bitwise AND
            min_path_cost[target_root] &= weight
            
            if source_root != target_root:
                min_path_cost[target_root] &= min_path_cost[source_root]
                parent[source_root] = target_root  # Merge sets
        
        result = []
        # Answering queries
        for start, end in query:
            if start == end:
                result.append(0)  # Same node, cost is 0
            elif find_root(start) != find_root(end):
                result.append(-1)  # Not connected
            else:
                result.append(min_path_cost[find_root(start)])  # Return min cost in component
                
        return result
