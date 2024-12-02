# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

# Example 1:
# Input: n = 5, queries = [[2,4],[0,2],[0,4]]
# Output: [3,2,1]
# Explanation:
# After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.
# After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.
# After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

from typing import List
from collections import defaultdict, deque
class Solution:
    def propagateUpdatedDistances(self, graph, currentNode, distances):
        """
        Propagates distance updates through the graph recursively from the current node.

        Args:
        - graph: The adjacency list representation of the graph.
        - currentNode: The node from which distance updates are propagated.
        - distances: The list storing the shortest distances from each node to the destination (n-1).
        """
        newDistance = distances[currentNode] + 1

        for neighbor in graph[currentNode]:
            # Skip if the current calculated distance is greater than or equal to the existing distance
            if distances[neighbor] <= newDistance:
                continue

            # Update the neighbor's distance
            distances[neighbor] = newDistance
            # Recursively propagate the updated distance
            self.propagateUpdatedDistances(graph, neighbor, distances)

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Computes the shortest distance from node 0 to node n-1 after each query.

        Args:
        - n: The number of nodes in the graph.
        - queries: A list of directed edges [source, target] to be added to the graph.

        Returns:
        - A list of the shortest distances from node 0 to node n-1 after processing each query.
        """
        # Initialize distances from each node to the destination (n-1)
        distances = [n - 1 - i for i in range(n)]

        # Initialize an adjacency list for the graph
        adjacencyList = [[] for _ in range(n)]
        
        # Pre-fill the graph with the initial edges pointing to the previous node
        for i in range(n - 1):
            adjacencyList[i + 1].append(i)

        # Result to store the shortest distances after each query
        shortestDistancesAfterQueries = []

        # Process each query (add edge and update distances)
        for source, target in queries:
            # Add the new edge to the graph
            adjacencyList[target].append(source)

            # Update the distance for the source node based on the target's distance
            distances[source] = min(distances[source], distances[target] + 1)
            
            # Propagate the updated distances through the graph
            self.propagateUpdatedDistances(adjacencyList, source, distances)

            # Append the shortest distance from node 0 to n-1
            shortestDistancesAfterQueries.append(distances[0])

        return shortestDistancesAfterQueries
