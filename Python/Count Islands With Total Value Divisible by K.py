# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

# Example 1:
# Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
# Output: 2
# Explanation:
# The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

class Solution:
    def countIslands(self, grid, k):
        # Get the number of rows and columns.
        m, n = len(grid), len(grid[0])

        # Define the four possible movement directions.
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # Count the islands whose total sum is divisible by k.
        ans = 0

        # Traverse every cell in the grid.
        for i in range(m):
            for j in range(n):
                # A positive value represents an unvisited land cell.
                if grid[i][j] > 0:
                    # Initialize the island's sum with the current cell's value.
                    total = grid[i][j]

                    # Mark the cell as visited by setting it to 0.
                    grid[i][j] = 0

                    # Use a stack to explore all connected land cells.
                    stack = [(i, j)]

                    while stack:
                        # Get the next cell to process.
                        r, c = stack.pop()

                        # Check all four adjacent cells.
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc

                            # If the neighbor is within bounds and contains unvisited land:
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                # Add its value to the island's total.
                                total += grid[nr][nc]

                                # Mark it as visited to prevent processing it again.
                                grid[nr][nc] = 0

                                # Add the neighbor to the stack for further exploration.
                                stack.append((nr, nc))

                    # Count the island if its total sum is divisible by k.
                    if total % k == 0:
                        ans += 1

        # Return the number of qualifying islands.
        return ans