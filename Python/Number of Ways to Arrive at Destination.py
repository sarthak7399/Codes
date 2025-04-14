# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

# Example 1:
# Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# Output: 4
# Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
# The four ways to get there in 7 minutes are:
# - 0 ➝ 6
# - 0 ➝ 4 ➝ 6
# - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
# - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Create adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Distance array to store shortest path to each node
        dist = [float('inf')] * n  
        # Ways array to count the number of shortest paths to each node
        ways = [0] * n  
        
        dist[0] = 0  # Distance to the source node (0) is 0
        ways[0] = 1  # There's one way to reach the source node
        
        # Min-heap for Dijkstra's algorithm (distance, node)
        pq = [(0, 0)]  
        
        MOD = 10**9 + 7  # Modulo for large numbers
        
        # Dijkstra's algorithm to find shortest paths
        while pq:
            d, node = heapq.heappop(pq)  # Get the node with the smallest distance
            
            if d > dist[node]:  # Skip if a shorter path was already found
                continue
                
            for neighbor, time in graph[node]:
                # Found a shorter path to the neighbor
                if dist[node] + time < dist[neighbor]:
                    dist[neighbor] = dist[node] + time
                    ways[neighbor] = ways[node]  # Inherit path count
                    heapq.heappush(pq, (dist[neighbor], neighbor))
                # Found another shortest path to the neighbor
                elif dist[node] + time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n - 1]  # Return the number of ways to reach the last node
