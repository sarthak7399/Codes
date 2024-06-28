# https://leetcode.com/problems/maximum-total-importance-of-roads/

# Example 1:
# Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
# Output: 43
# Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
# - The road (0,1) has an importance of 2 + 4 = 6.
# - The road (1,2) has an importance of 4 + 5 = 9.
# - The road (2,3) has an importance of 5 + 3 = 8.
# - The road (0,2) has an importance of 2 + 5 = 7.
# - The road (1,3) has an importance of 4 + 3 = 7.
# - The road (2,4) has an importance of 5 + 1 = 6.
# The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
# It can be shown that we cannot obtain a greater total importance than 43.

from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        total_importance = 0  # Total importance of all cities
        importance_value = 1  # Initial importance value to assign
        connections = [0] * n  # List to store the number of connections for each city
        
        # Count the number of connections for each city
        for road in roads:
            connections[road[0]] += 1
            connections[road[1]] += 1
        
        # Sort the connections to assign higher importance to more connected cities
        connections.sort()
        
        # Calculate the total importance based on sorted connections
        for connection_count in connections:
            total_importance += connection_count * importance_value
            importance_value += 1
        
        return total_importance
