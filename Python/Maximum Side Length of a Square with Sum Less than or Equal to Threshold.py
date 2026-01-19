# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

# Example 1:
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Prefix sum: prefix[i][j] = sum of submatrix (0,0) to (i-1,j-1)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        # Binary search on the side length
        left, right, ans = 0, min(m, n), 0

        while left <= right:
            mid = (left + right) // 2  # candidate side length
            found = False

            # Check if any mid x mid square has sum <= threshold
            for i in range(mid, m + 1):
                for j in range(mid, n + 1):
                    total = (
                        prefix[i][j]
                        - prefix[i - mid][j]
                        - prefix[i][j - mid]
                        + prefix[i - mid][j - mid]
                    )
                    if total <= threshold:
                        found = True
                        break
                if found:
                    break

            if found:
                ans = mid          # mid is possible, try bigger
                left = mid + 1
            else:
                right = mid - 1    # mid not possible, try smaller

        return ans
