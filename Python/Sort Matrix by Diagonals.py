# https://leetcode.com/problems/sort-matrix-by-diagonals/

# Example 1:
# Input: grid = [[1,7,3],[9,8,2],[4,5,6]]
# Output: [[8,2,3],[9,6,7],[4,5,1]]
# Explanation:
# The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:
# [1, 8, 6] becomes [8, 6, 1].
# [9, 5] and [4] remain unchanged.
# The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:
# [7, 2] becomes [2, 7].
# [3] remains unchanged.

from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        import heapq
        n, m = len(grid), len(grid[0])   # Get dimensions of the matrix
        diags = {}                       # Dictionary to store diagonals by key (i - j)

        # Step 1: Group elements into diagonals based on (i - j)
        for i in range(n):
            for j in range(m):
                key = i - j              # Diagonal identifier (same i-j => same diagonal)
                if key not in diags:
                    diags[key] = []

                # If key < 0 (upper-right diagonals) → store elements in min-heap
                if key < 0:
                    heapq.heappush(diags[key], grid[i][j])
                # If key >= 0 (lower-left diagonals) → store elements as negative in min-heap 
                # (acts as a max-heap to get descending order)
                else:
                    heapq.heappush(diags[key], -grid[i][j])

        # Step 2: Reconstruct the matrix by popping values from heaps
        for i in range(n):
            for j in range(m):
                key = i - j
                # For upper-right diagonals → pop smallest from min-heap
                if key < 0:
                    grid[i][j] = heapq.heappop(diags[key])
                # For lower-left diagonals → pop largest (by negating back)
                else:
                    grid[i][j] = -heapq.heappop(diags[key])

        return grid
