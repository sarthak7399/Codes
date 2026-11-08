# https://leetcode.com/problems/count-servers-that-communicate/

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.

from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Count the number of servers (1s) in each row.
        Rows = [sum(row) for row in grid]

        # Count the number of servers (1s) in each column.
        Col = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]

        # Count a server if it can communicate with at least one other server
        # in the same row or column.
        return sum(
            1 for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j] == 1 and (Rows[i] > 1 or Col[j] > 1)
        )