# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

# Example 1:
# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
# Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
# There are a total of 7 unguarded cells, so we return 7.

from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid
        grid = [[0 for i in range(n)] for j in range(m)]
        
        # Constants for marking the grid
        guard = 1
        wall = 2
        guarded = 3
        
        # Place guards on the grid
        for i, j in guards:
            grid[i][j] = guard

        # Place walls on the grid
        for i, j in walls:
            grid[i][j] = wall

        # Mark all cells guarded by each guard
        for currentGuard in guards:
            i, j = currentGuard

            # Guard downwards
            while i + 1 < m and grid[i+1][j] not in [guard, wall]:
                grid[i+1][j] = guarded
                i += 1
            
            # Guard rightwards
            i, j = currentGuard  # Reset to original guard position
            while j + 1 < n and grid[i][j+1] not in [guard, wall]:
                grid[i][j+1] = guarded
                j += 1
            
            # Guard upwards
            i, j = currentGuard  # Reset to original guard position
            while i - 1 >= 0 and grid[i-1][j] not in [guard, wall]:
                grid[i-1][j] = guarded
                i -= 1
            
            # Guard leftwards
            i, j = currentGuard  # Reset to original guard position
            while j - 1 >= 0 and grid[i][j-1] not in [guard, wall]:
                grid[i][j-1] = guarded
                j -= 1

        # # Debug: Print the grid (optional for visualization)
        # for row in grid:
        #     print(" ".join(map(str, row)))

        # Count unguarded cells
        unguarded_count = sum(row.count(0) for row in grid)
        return unguarded_count
