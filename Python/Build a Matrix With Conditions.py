# https://leetcode.com/problems/build-a-matrix-with-conditions/

# Example 1:
# Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
# Output: [[3,0,0],[0,0,1],[0,2,0]]
# Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
# The row conditions are the following:
# - Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
# - Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
# The column conditions are the following:
# - Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
# - Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
# Note that there may be multiple correct answers.

from collections import defaultdict
from typing import List
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Create graph and indegree lists for rows and columns
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        row_indegree = [0] * (k + 1)
        col_indegree = [0] * (k + 1)

        # Add row conditions to the graph and update indegree
        for condition in rowConditions:
            above, below = condition
            row_graph[above].append(below)
            row_indegree[below] += 1

        # Add column conditions to the graph and update indegree
        for condition in colConditions:
            left, right = condition
            col_graph[left].append(right)
            col_indegree[right] += 1

        # Perform topological sort on rows and columns
        row_order = self.topological_sort(row_graph, row_indegree, k)
        if row_order is None:
            return []
        
        col_order = self.topological_sort(col_graph, col_indegree, k)
        if col_order is None:
            return []

        # Create matrix and position dictionaries
        matrix = [[0] * k for _ in range(k)]
        row_position = {}
        col_position = {}

        # Update row and column positions
        for i, node in enumerate(row_order):
            row_position[node] = i

        for i, node in enumerate(col_order):
            col_position[node] = i

        # Fill the matrix with the nodes in the correct positions
        for i in range(1, k + 1):
            if i in row_position and i in col_position:
                row_idx = row_position[i]
                col_idx = col_position[i]
                matrix[row_idx][col_idx] = i

        return matrix

    def topological_sort(self, graph, indegree, n):
        queue = [i for i in range(1, n + 1) if indegree[i] == 0]
        order = []
        while queue:
            node = queue.pop(0)
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == n else None