# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

# Example 1:
# Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
# Output: [228,216,211]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
# - Blue: 20 + 3 + 200 + 5 = 228
# - Red: 200 + 2 + 10 + 4 = 216
# - Green: 5 + 200 + 4 + 2 = 211

from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        # Grid dimensions
        m, n = len(grid), len(grid[0])
        
        # Maximum possible rhombus radius
        # Limited by grid height and width
        max_length = min((m - 1) // 2, (n - 1) // 2)
        
        # Min heap to keep the top 3 largest distinct sums
        best = []
        heapify(best)

        # Function to compute the boundary sum of a rhombus
        # r, c = top vertex of rhombus
        # k = radius (distance from center to each corner)
        def rhombusSum(r, c, k):
            
            # Start with the top vertex
            result = grid[r][c]

            # Traverse the upper half edges of rhombus
            for s in range(k):
                r += 1
                
                # Right-down diagonal
                result += grid[r][c + s + 1]
                
                # Left-down diagonal
                result += grid[r][c - s - 1]

            # Traverse the lower half edges of rhombus
            for s in range(k - 1, -1, -1):
                r += 1
                
                # Right-up diagonal
                result += grid[r][c + s]
                
                # Left-up diagonal
                if s > 0:  # Avoid double counting bottom corner
                    result += grid[r][c - s]

            return result

        # Iterate through each cell as potential top vertex
        for r in range(m):
            for c in range(n):

                # Try all possible rhombus sizes
                for k in range(max_length + 1):

                    # Check if rhombus stays inside grid boundaries
                    if c >= k and c + k < n and r + 2 * k < m:

                        # Calculate rhombus boundary sum
                        candidate = rhombusSum(r, c, k)

                        # Ensure we only keep distinct sums
                        if candidate not in set(best):
                            heappush(best, candidate)

                        # Maintain only the top 3 values in heap
                        if len(best) > 3:
                            heappop(best)

        # Return results in descending order
        return sorted(best, reverse=True)