# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

# Example 1:
# Input: grid = [[1,0,1],[1,1,1]]
# Output: 5
# Explanation:
# The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
# The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
# The 1 at (1, 1) is covered by a rectangle of area 1.

from functools import cache
from typing import List

class Solution: 
    def minimumSum(self, grid: List[List[int]]) -> int:
        # A helper function (memoized with @cache) that finds the minimum
        # enclosing rectangle area containing all '1's inside a given subgrid
        # bounded by rows [a..b] and columns [c..d].
        @cache
        def helper(a, b, c, d):
            # Initialize boundaries of rectangle
            mii, mij = float('inf'), float('inf')   # min row, min col (top-left corner)
            mai, maj = -float('inf'), -float('inf') # max row, max col (bottom-right corner)

            # Traverse subgrid to find bounding box of all '1's
            for i in range(a, b+1):
                for j in range(c, d+1):
                    if grid[i][j] == 1:
                        mii, mij = min(mii, i), min(mij, j)
                        mai, maj = max(mai, i), max(maj, j)

            # If no '1' found, area is 0 (since mai/mii, maj/mij remain infinities,
            # but problem constraints usually guarantee at least one '1' per partition)
            return (mai - mii + 1) * (maj - mij + 1)

        m, n = len(grid), len(grid[0])  # Grid dimensions
        res = 99999  # Initialize answer with a large value

        # -------------------------------
        # CASE 1: Split the grid into 3 horizontal strips
        # -------------------------------
        for i in range(m-1):
            for j in range(i+1, m-1):
                res = min(
                    helper(0, i, 0, n-1) +       # Top strip
                    helper(i+1, j, 0, n-1) +     # Middle strip
                    helper(j+1, m-1, 0, n-1),    # Bottom strip
                    res
                )

        # -------------------------------
        # CASE 2: Split the grid into 3 vertical strips
        # -------------------------------
        for i in range(n-1):
            for j in range(i+1, n-1):
                res = min(
                    helper(0, m-1, 0, i) +       # Left strip
                    helper(0, m-1, i+1, j) +     # Middle strip
                    helper(0, m-1, j+1, n-1),    # Right strip
                    res
                )

        # -------------------------------
        # CASE 3: Split the grid into L-shaped partitions (2 cuts)
        # This tries different "corner" configurations to make 3 regions
        # -------------------------------
        for i in range(m-1):
            for j in range(n-1):
                # Partition type 1: top row block + bottom-left + bottom-right
                res = min(
                    helper(0, i, 0, n-1) +       # Top rectangle
                    helper(i+1, m-1, 0, j) +     # Bottom-left rectangle
                    helper(i+1, m-1, j+1, n-1),  # Bottom-right rectangle
                    res
                )
                # Partition type 2: left col block + top-right + bottom-right
                res = min(
                    helper(0, m-1, 0, j) +       # Left rectangle
                    helper(0, i, j+1, n-1) +     # Top-right rectangle
                    helper(i+1, m-1, j+1, n-1),  # Bottom-right rectangle
                    res
                )
                # Partition type 3: top-left + top-right + bottom
                res = min(
                    helper(0, i, 0, j) +         # Top-left rectangle
                    helper(0, i, j+1, n-1) +     # Top-right rectangle
                    helper(i+1, m-1, 0, n-1),    # Bottom rectangle
                    res
                )
                # Partition type 4: top-left + bottom-left + right
                res = min(
                    helper(0, i, 0, j) +         # Top-left rectangle
                    helper(i+1, m-1, 0, j) +     # Bottom-left rectangle
                    helper(0, m-1, j+1, n-1),    # Right rectangle
                    res
                )               

        return res
