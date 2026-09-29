# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

# Example 1:
# Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
# Output: true
# Explanation: The above diagram shows two possible paths that form valid parentheses strings.
# The first path shown results in the valid parentheses string "()(())".
# The second path shown results in the valid parentheses string "((()))".
# Note that there may be other valid parentheses string paths.

from functools import lru_cache
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        # Get the number of rows and columns in the grid.
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row, col, balance):
            # Return False if we move outside the grid.
            if row >= m or col >= n:
                return False

            # Update the balance based on the current cell.
            # '(' increases the balance and ')' decreases it.
            balance += 1 if grid[row][col] == '(' else -1

            # A negative balance means there are more closing
            # parentheses than opening parentheses.
            if balance < 0:
                return False

            # At the destination, the path is valid only if
            # all opening parentheses have been closed.
            if row == m - 1 and col == n - 1:
                return balance == 0

            # Try moving down or right.
            return (
                dfs(row + 1, col, balance) or
                dfs(row, col + 1, balance)
            )

        # Start DFS from the top-left cell with balance 0.
        return dfs(0, 0, 0)