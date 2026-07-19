# https://leetcode.com/problems/minimum-time-visiting-all-points/

# Example 1:
# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0  # total time required

        for i in range(1, len(points)):
            # Distance between two points = max(dx, dy)
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])

            ans += max(dx, dy)

        return ans
