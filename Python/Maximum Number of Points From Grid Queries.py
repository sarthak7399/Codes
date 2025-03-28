# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

# Example 1:
# Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# Output: [5,8,1]
# Explanation: The diagrams above show which cells we visit to get points for each query.

from queue import PriorityQueue

class Solution:
    def maxPoints(self, grid, queries):
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        # Store queries with their original indices and sort them by value
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        result = [0] * len(queries)  # Store results for each query
        
        heap = PriorityQueue()  # Min-heap to track visited grid cells
        visited = [[False] * cols for _ in range(rows)]  # Track visited cells
        
        heap.put((grid[0][0], 0, 0))  # Start with the top-left cell
        visited[0][0] = True
        points = 0  # Count of points collected
        
        # Process each query in increasing order
        for query_val, query_idx in sorted_queries:
            while not heap.empty() and heap.queue[0][0] < query_val:
                _, row, col = heap.get()
                points += 1  # Increment points when expanding a valid cell
                
                # Explore all four possible directions
                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        not visited[nr][nc]):
                        heap.put((grid[nr][nc], nr, nc))
                        visited[nr][nc] = True  # Mark cell as visited
            
            result[query_idx] = points  # Store the result for the query
        
        return result
