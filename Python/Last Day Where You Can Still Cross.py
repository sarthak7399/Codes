# https://leetcode.com/problems/last-day-where-you-can-still-cross/

# Example 1:
# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # Total nodes = all cells + 2 virtual nodes (West and East)
        n = len(cells) + 2
        root = [i for i in range(n)]
        rank = [1] * n
        isWater = [False] * n

        # Find with path compression
        def Find(x):
            if x != root[x]:
                root[x] = Find(root[x])
            return root[x]

        # Union by rank
        def Union(x, y):
            x, y = Find(x), Find(y)
            if x == y:
                return
            if rank[x] > rank[y]:
                x, y = y, x
            root[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

        # Check if two nodes are connected
        def connected(x, y):
            return Find(x) == Find(y)

        # Map 2D cell to 1D index
        def key(i, j):
            return (i - 1) * col + j - 1

        # Virtual nodes for left and right borders
        East, West = n - 2, n - 1

        # Process cells day by day
        for t, (i, j) in enumerate(cells):
            idx0 = key(i, j)
            isWater[idx0] = True

            # Connect to virtual borders if on left/right edge
            if j == 1:
                Union(West, idx0)
            if j == col:
                Union(East, idx0)

            # All 8 possible neighbors
            adj = (
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
                (i, j + 1), (i - 1, j + 1), (i - 1, j),
                (i - 1, j - 1), (i, j - 1)
            )

            # Union with adjacent water cells
            for a, b in adj:
                if a <= 0 or a > row or b <= 0 or b > col:
                    continue
                idx1 = key(a, b)
                if not isWater[idx1]:
                    continue
                Union(idx0, idx1)

                # If left and right borders are connected, crossing is blocked
                if connected(East, West):
                    return t

        return 0
