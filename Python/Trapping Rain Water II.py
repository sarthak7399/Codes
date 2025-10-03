# https://leetcode.com/problems/trapping-rain-water-ii/

# Example 1:
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.

class Solution:
    def trapRainWater(self, height: List[List[int]]) -> int:
        dir = (0, 1, 0, -1, 0)   # direction offsets for 4-neighbours (right, down, left, up)
        m, n = len(height), len(height[0])
        if m <= 2 or n <= 2:
            return 0   # too small to trap water

        boundary = []   # min-heap for boundary cells (height, i, j)

        # push left & right columns as boundary
        for i in range(m):
            boundary.append((height[i][0], i, 0))
            boundary.append((height[i][-1], i, n - 1))
            height[i][0] = height[i][-1] = -1  # mark as visited

        # push top & bottom rows as boundary
        for j in range(1, n - 1):
            boundary.append((height[0][j], 0, j))
            boundary.append((height[-1][j], m - 1, j))
            height[0][j] = height[-1][j] = -1  # mark visited

        heapify(boundary)  # min-heap of boundary
        ans, water_level = 0, 0

        # process cells from lowest boundary upwards
        while boundary:
            h, i, j = heappop(boundary)
            water_level = max(water_level, h)  # current max water level

            # explore 4-neighbours
            for a in range(4):
                i0, j0 = i + dir[a], j + dir[a + 1]
                if i0 < 0 or i0 >= m or j0 < 0 or j0 >= n or height[i0][j0] == -1:
                    continue

                currH = height[i0][j0]
                if currH < water_level:
                    ans += water_level - currH   # trapped water

                height[i0][j0] = -1   # mark visited
                heappush(boundary, (currH, i0, j0))  # push into heap

        return ans   # total trapped water
