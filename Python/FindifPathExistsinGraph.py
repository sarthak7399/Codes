# https://leetcode.com/problems/find-if-path-exists-in-graph/

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

class Solution(object):
    def validPath(self, n, edges, source, destination):
        if n == 1:
            return True  # Special case where there is only one vertex
        visited = [False] * n  # Mark all vertices as not visited initially
        visited[source] = True  # Mark the source vertex as visited
        flag = True  # Initialize a flag to control the loop
        while flag:  # Continue loop until flag becomes False
            flag = False  # Reset the flag
            for edge in edges:  # Iterate over all edges
                if visited[edge[0]] != visited[edge[1]]:  # If one vertex is visited and other is not
                    visited[edge[0]] = True  # Mark both vertices as visited
                    visited[edge[1]] = True
                    flag = True  # Set the flag to continue the loop
                if visited[destination]:  # If destination vertex is visited
                    return True  # Return True, as path exists
        return False  # If loop exits without finding path, return False
