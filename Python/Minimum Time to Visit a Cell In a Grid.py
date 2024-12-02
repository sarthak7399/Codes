# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

# Example 1:
# Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
# Output: 7
# Explanation: One of the paths that we can take is the following:
# - at t = 0, we are on the cell (0,0).
# - at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
# - at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
# - at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
# - at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
# - at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
# - at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
# - at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
# The final time is 7. It can be shown that it is the minimum time possible.

from heapq import heappop, heappush
from typing import List
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # Define possible moves: up, right, down, left
        MOVES = ((-1, 0), (0, 1), (1, 0), (0, -1))
        
        # Check if the starting point has a valid path to move
        # If both potential starting moves are blocked (>1), there's no valid path
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
            
        rows, cols = len(grid), len(grid[0])
        
        # Priority queue for Dijkstra-like BFS
        # Each element is a tuple: (time, row, col)
        pq = [(0, 0, 0)]  # Start at time=0, position=(0, 0)
        
        # Visited matrix to track cells we've already processed
        seen = [[False] * cols for _ in range(rows)]
        seen[0][0] = True  # Mark the starting cell as visited
        
        # Process the grid using BFS with a priority queue
        while pq:
            # Get the cell with the smallest time value
            time, row, col = heappop(pq)
            
            # Explore all possible moves from the current cell
            for dr, dc in MOVES:
                newRow, newCol = row + dr, col + dc
                
                # Check if the new cell is within bounds and hasn't been visited
                if (newRow < 0 or newRow >= rows or 
                    newCol < 0 or newCol >= cols or 
                    seen[newRow][newCol]):
                    continue
                
                # Compute the earliest possible time to move to the new cell
                newTime = time + 1
                
                # If the cell's constraint (`grid[newRow][newCol]`) exceeds the time, adjust the time
                if grid[newRow][newCol] > newTime:
                    # Calculate the next valid time to enter the cell, considering even-odd parity
                    newTime += (grid[newRow][newCol] - time) // 2 * 2
                
                # If the destination cell (bottom-right) is reached, return the time
                if newRow == rows - 1 and newCol == cols - 1:
                    return newTime
                    
                # Mark the new cell as visited and add it to the priority queue
                seen[newRow][newCol] = True
                heappush(pq, (newTime, newRow, newCol))
        
        # If the queue is exhausted without reaching the bottom-right cell, return -1
        return -1