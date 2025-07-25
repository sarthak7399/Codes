# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

# Example 1:
# Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
# Output: 4
# Explanation: As shown in the image we:
# - Add node 5 to the first group.
# - Add node 1 to the second group.
# - Add nodes 2 and 4 to the third group.
# - Add nodes 3 and 6 to the fourth group.
# We can see that every edge is satisfied.
# It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

from collections import deque
class Solution:
    # Checks if the graph is bipartite starting from the given node
    def is_bipartite(self, adj_list, node, colors):
        for neighbor in adj_list[node]:
            # If a neighbor has the same color as the current node, the graph is not bipartite
            if colors[neighbor] == colors[node]:
                return False
            # If the neighbor is already colored, skip it
            if colors[neighbor] != -1:
                continue
            # Assign the opposite color to the neighbor
            colors[neighbor] = (colors[node] + 1) % 2
            # Recursively check bipartiteness for the neighbor; return false if it fails
            if not self.is_bipartite(adj_list, neighbor, colors):
                return False
        # If all neighbors are properly colored, return true
        return True

    # Computes the longest shortest path (height) in the graph starting from the source node
    def get_longest_shortest_path(self, adj_list, src_node, n):
        # Initialize a queue for BFS and a visited array
        nodes_queue = deque([src_node])
        visited = [False] * n
        visited[src_node] = True
        distance = 0

        # Perform BFS layer by layer
        while nodes_queue:
            # Process all nodes in the current layer
            for _ in range(len(nodes_queue)):
                current_node = nodes_queue.popleft()
                # Visit all unvisited neighbors of the current node
                for neighbor in adj_list[current_node]:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    nodes_queue.append(neighbor)
            # Increment the distance for each layer
            distance += 1

        # Return the total distance (longest shortest path)
        return distance

    # Calculates the maximum number of groups for a connected component
    def get_number_of_groups_for_component(
        self, adj_list, node, distances, visited
    ):
        # Start with the distance of the current node as the maximum
        max_number_of_groups = distances[node]
        visited[node] = True

        # Recursively calculate the maximum for all unvisited neighbors
        for neighbor in adj_list[node]:
            if visited[neighbor]:
                continue
            max_number_of_groups = max(
                max_number_of_groups,
                self.get_number_of_groups_for_component(
                    adj_list, neighbor, distances, visited
                ),
            )
        return max_number_of_groups

    # Main function to calculate the maximum number of magnificent sets
    def magnificentSets(self, n, edges):
        # Create adjacency list for the graph
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            # Transition to 0-index
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        # Initialize color array to -1
        colors = [-1] * n

        # Check if the graph is bipartite
        for node in range(n):
            if colors[node] != -1:
                continue
            # Start coloring from uncolored nodes
            colors[node] = 0
            if not self.is_bipartite(adj_list, node, colors):
                return -1

        # Calculate the longest shortest path for each node
        distances = [
            self.get_longest_shortest_path(adj_list, node, n)
            for node in range(n)
        ]

        # Calculate the total maximum number of groups across all components
        max_number_of_groups = 0
        visited = [False] * n
        for node in range(n):
            if visited[node]:
                continue
            # Add the number of groups for this component to the total
            max_number_of_groups += self.get_number_of_groups_for_component(
                adj_list, node, distances, visited
            )

        return max_number_of_groups