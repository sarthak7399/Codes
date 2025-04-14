# https://leetcode.com/problems/course-schedule-iv/

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
# Course 0 is not a prerequisite of course 1, but the opposite is true.

from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create an adjacency list to represent the graph
        adj = [[] for _ in range(numCourses)]
        
        # Build the graph based on the prerequisites list
        # Each pair (a, b) means that course b is a prerequisite for course a
        for a, b in prerequisites:
            adj[a].append(b)

        # Initialize a 2D list 'reachable' to track if a course can be reached from another course
        # reachable[i][j] will be True if course j is reachable from course i
        reachable = [[False] * numCourses for _ in range(numCourses)]

        # Depth First Search (DFS) function to find all reachable courses from the 'start' course
        def dfs(start, node):
            reachable[start][node] = True  # Mark the current node as reachable from the 'start' course
            for neighbor in adj[node]:  # Explore all neighboring nodes (prerequisites of the current course)
                if not reachable[start][neighbor]:  # If the neighbor hasn't been visited yet
                    dfs(start, neighbor)  # Recursively visit the neighbor
                    
        # Perform DFS for each course to find all reachable courses
        for i in range(numCourses):
            dfs(i, i)  # Start DFS from course i to find all its reachable courses
            
        # Prepare the result for each query
        res = []
        for a, b in queries:
            # Append the result of whether course b is a prerequisite of course a
            res.append(reachable[a][b])

        return res  # Return the list of results for all queries
