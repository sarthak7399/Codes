# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

# Example 1:
# Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
# Output: [8,7,7,8,8]
# Explanation:
# For i = 0, connect node 0 from the first tree to node 0 from the second tree.
# For i = 1, connect node 1 from the first tree to node 4 from the second tree.
# For i = 2, connect node 2 from the first tree to node 7 from the second tree.
# For i = 3, connect node 3 from the first tree to node 0 from the second tree.
# For i = 4, connect node 4 from the first tree to node 4 from the second tree.

from collections import deque

class Solution(object):
    def buildGraph(self, edges, size):
        """
        Builds an undirected graph from edge list.

        :param edges: List of [u, v] edges.
        :param size: Total number of nodes in the graph.
        :return: Adjacency list of the graph.
        """
        graph = [[] for _ in range(size)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def bfs(self, graph):
        """
        Performs BFS and 2-colors the graph (like bipartite coloring),
        while counting the number of nodes in each color group.

        :param graph: Adjacency list of the graph.
        :return: Tuple (color_count, node_color)
                 - color_count: [count of color 0, count of color 1]
                 - node_color: color assigned to each node
        """
        n = len(graph)
        color_count = [0, 0]         # Count of nodes with color 0 and color 1
        node_color = [0] * n         # Color assigned to each node
        visited = [False] * n
        queue = deque([(0, 0)])      # (node, color)
        visited[0] = True

        while queue:
            node, color = queue.popleft()
            node_color[node] = color
            color_count[color] += 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, 1 - color))  # Alternate color

        return color_count, node_color

    def maxTargetNodes(self, edges1, edges2):
        """
        Combines two trees:
        - Applies bipartite coloring to both.
        - For each node in tree1, calculates max reachable nodes from corresponding group in tree2.

        :param edges1: Edges of first tree (tree1).
        :param edges2: Edges of second tree (tree2).
        :return: List with maximum target nodes each node in tree1 can reach via same-colored nodes + tree2 max group.
        """
        n = len(edges1) + 1  # Nodes in tree1
        m = len(edges2) + 1  # Nodes in tree2

        # Build both trees as adjacency lists
        tree1 = self.buildGraph(edges1, n)
        tree2 = self.buildGraph(edges2, m)

        # Run BFS on both trees to color and count nodes
        color1, node_color1 = self.bfs(tree1)
        color2, _ = self.bfs(tree2)

        max_color2 = max(color2)  # Pick the larger group from tree2 to maximize targets

        # For each node in tree1, assign result based on its color group and tree2's largest group
        result = [0] * n
        for i in range(n):
            result[i] = color1[node_color1[i]] + max_color2

        return result
