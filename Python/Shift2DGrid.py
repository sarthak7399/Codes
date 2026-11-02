# https://leetcode.com/problems/shift-2d-grid/

# Example 2:
# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Get the number of rows and columns.
        m = len(grid)
        n = len(grid[0])

        # Split k into:
        # q = complete row shifts
        # r = additional column shifts
        q, r = divmod(k, n)

        # Since shifting by m complete rows brings the grid
        # back to its original row position, take q modulo m.
        q %= m

        # Create the result grid.
        ans = [[0] * n for _ in range(m)]

        # Process every element of the original grid.
        for i in range(m):
            # Calculate the starting row after shifting.
            i1 = i + q + 1

            for j in range(n):
                # If j + r is less than n, the element stays
                # in the same shifted row.
                minus1 = j + r < n

                # Calculate the new column position.
                j0 = j + r

                # Wrap around to the first column if needed.
                if j0 >= n:
                    j0 -= n

                # Calculate the new row position.
                i0 = i1 - minus1

                # Wrap around to the first row if needed.
                if i0 >= m:
                    i0 -= m

                # Place the current element at its new position.
                ans[i0][j0] = grid[i][j]

        return ans