# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

# Example 2:
# Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4
# Output: 1
# Explanation:
# Select the points (0, 0), (2, 0), (2, 2), and (2, 1).

from bisect import bisect_left
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        res = []  # Will store 1D positions of points along the square perimeter

        # Convert 2D boundary points into 1D positions (unrolling the square)
        for x, y in points:
            if x == 0:
                res.append(y)  # Left edge (bottom → top)
            elif y == side:
                res.append(side + x)  # Top edge (left → right)
            elif x == side:
                res.append(side * 3 - y)  # Right edge (top → bottom)
            else:
                res.append(side * 4 - x)  # Bottom edge (right → left)

        # Sort positions on the perimeter
        res.sort()

        # Check if we can place k points with at least distance 'n'
        def check(n: int) -> bool:
            idx = [0] * k  # Stores indices of chosen points
            curr = res[0]  # Start from the first point

            # Greedily pick next points with distance >= n
            for i in range(1, k):
                j = bisect_left(res, curr + n)  # Find next valid position
                if j == len(res):
                    return False  # No valid next point
                idx[i] = j
                curr = res[j]

            # Check circular condition (wrap-around distance)
            if curr - res[0] <= side * 4 - n:
                return True
            
            # Try shifting starting point to find valid configuration
            for idx[0] in range(1, idx[1]):
                for j in range(1, k):
                    # Move pointer forward until distance condition is satisfied
                    while res[idx[j]] < res[idx[j - 1]] + n:
                        idx[j] += 1
                        if idx[j] == len(res):
                            return False
                
                # Check circular condition again
                if res[idx[-1]] - res[idx[0]] <= side * 4 - n:
                    return True

            return False
        
        # Binary search on answer (maximum minimum distance)
        left, right = 1, side + 1

        while left + 1 < right:
            mid = (left + right) // 2

            # If feasible, try larger distance
            if check(mid):
                left = mid
            else:
                right = mid

        return left  # Maximum minimum distance achievable