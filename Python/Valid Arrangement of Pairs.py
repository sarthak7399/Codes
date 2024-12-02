# https://leetcode.com/problems/valid-arrangement-of-pairs/

# Example 1:
# Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
# Output: [[11,9],[9,4],[4,5],[5,1]]
# Explanation:
# This is a valid arrangement since endi-1 always equals starti.
# end0 = 9 == 9 = start1 
# end1 = 4 == 4 = start2
# end2 = 5 == 5 = start3

from collections import defaultdict
from typing import List
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # `graph` stores the adjacency list representation of the directed graph
        # `inOutDeg` keeps track of the in-degree and out-degree differences for each node
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        # Step 1: Build the graph and calculate in/out degree for each node
        for start, end in pairs:
            graph[start].append(end)  # Add a directed edge from 'start' to 'end'
            inOutDeg[start] += 1      # Increment out-degree for the start node
            inOutDeg[end] -= 1        # Decrement in-degree for the end node

        # Step 2: Find the starting node for the Eulerian path
        # An Eulerian path starts at a node with out-degree = in-degree + 1, if such a node exists.
        startNode = pairs[0][0]  # Default to the first node in the pairs
        for node in inOutDeg:
            if inOutDeg[node] == 1:  # Node with out-degree greater than in-degree
                startNode = node
                break

        # Step 3: Initialize the path and perform a Depth-First Search (DFS)
        path = []  # This will store the Eulerian path as a list of edges

        # Recursive DFS function to traverse the graph
        def dfs(curr):
            # Continue while there are outgoing edges from the current node
            while graph[curr]:
                nextNode = graph[curr].pop()  # Remove the last edge to the next node
                dfs(nextNode)  # Recursively visit the next node
                path.append((curr, nextNode))  # Append the traversed edge to the path

        # Start DFS traversal from the determined starting node
        dfs(startNode)

        # Return the path in reverse order (since edges are added post-recursion)
        return path[::-1]
