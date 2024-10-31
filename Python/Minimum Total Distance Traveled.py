# https://leetcode.com/problems/minimum-total-distance-traveled/

# Example 1:
# Input: robot = [0,4,6], factory = [[2,2],[6,2]]
# Output: 4
# Explanation: As shown in the figure:
# - The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
# - The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
# - The third robot at position 6 will be repaired at the second factory. It does not need to move.
# The limit of the first factory is 2, and it fixed 2 robots.
# The limit of the second factory is 2, and it fixed 1 robot.
# The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.

from collections import deque
from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort positions to enable optimal matching
        robot.sort()
        factory.sort()
        
        m, n = len(robot), len(factory)
        # DP table initialization
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        # Base case: if no factories left, distance is infinite
        for i in range(m): 
            dp[i][-1] = float('inf')
        
        # Process each factory from right to left
        for j in range(n-1, -1, -1):
            prefix = 0
            qq = deque([(m, 0)])
            
            # Process each robot from right to left
            for i in range(m-1, -1, -1):
                # Add distance to current factory
                prefix += abs(robot[i] - factory[j][0])
                
                # Remove elements outside factory limit window
                if qq[0][0] > i+factory[j][1]: 
                    qq.popleft()
                
                # Maintain monotonic queue property
                while qq and qq[-1][1] >= dp[i][j+1] - prefix:
                    qq.pop()
                    
                qq.append((i, dp[i][j+1] - prefix))
                dp[i][j] = qq[0][1] + prefix
                
        return dp[0][0]