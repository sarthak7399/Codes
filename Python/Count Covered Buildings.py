# https://leetcode.com/problems/count-covered-buildings/

# Example 1:
# Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
# Output: 1
# Explanation:
# Only building [2,2] is covered as it has at least one building:
# above ([1,2])
# below ([3,2])
# left ([2,1])
# right ([2,3])
# Thus, the count of covered buildings is 1.

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Arrays to track min/max x for each y, and min/max y for each x
        xMax, yMax = [0] * (n + 1), [0] * (n + 1)
        xMin, yMin = [1 << 31] * (n + 1), [1 << 31] * (n + 1)

        # Populate boundary information for each row (y) and column (x)
        for x, y in buildings:
            xMin[y] = min(xMin[y], x)   # Leftmost building in this row
            xMax[y] = max(xMax[y], x)   # Rightmost building in this row
            yMin[x] = min(yMin[x], y)   # Bottom-most building in this column
            yMax[x] = max(yMax[x], y)   # Top-most building in this column

        cnt = 0
        for x, y in buildings:
            # Check if this building is covered horizontally:
            # x must lie strictly between min and max x in the same row
            coverX = (xMin[y] < x) & (x < xMax[y])

            # Check if covered vertically:
            # y must lie strictly between min and max y in the same column
            coverY = (yMin[x] < y) & (y < yMax[x])

            # Count if both conditions are true
            cnt += (coverX & coverY)

        return cnt
