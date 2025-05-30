# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

# Example 1:
# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2
# Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
# The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

class Solution:
    def dfs(self, edges, start):
        """
        Perform a DFS-like traversal on a directed graph where each node has at most one outgoing edge.

        :param edges: List[int] representing edges[i] = next node from node i (or -1 if no edge)
        :param start: Starting node for traversal
        :return: List[int] with distance from start node to every other node (-1 if not reachable)
        """
        dist = [-1] * len(edges)  # Distance array initialized to -1
        d = 0
        # Traverse until you reach a visited node or a dead end
        while start != -1 and dist[start] == -1:
            dist[start] = d
            d += 1
            start = edges[start]  # Move to next node in the edge chain
        return dist

    def closestMeetingNode(self, edges, node1, node2):
        """
        Find the node that is reachable from both node1 and node2 such that the maximum of the distances
        from node1 and node2 to that node is minimized.

        :param edges: Directed graph with at most one outgoing edge per node
        :param node1: First starting node
        :param node2: Second starting node
        :return: The closest meeting node index, or -1 if none exists
        """
        dist1 = self.dfs(edges, node1)  # Distance from node1 to all nodes
        dist2 = self.dfs(edges, node2)  # Distance from node2 to all nodes

        result = -1
        min_dist = float('inf')  # Minimum of the max distances from both nodes

        # Iterate through all nodes to find the optimal meeting node
        for i in range(len(edges)):
            # Node must be reachable from both node1 and node2
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])  # Max distance from either node
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i  # Update result with closer meeting node

        return result
