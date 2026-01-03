# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

# Example 1:
# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown.

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007
        
        # x: number of ways where a row has 3 different colours (ABC pattern)
        # y: number of ways where a row has 2 colours (ABA pattern)
        x, y = 6, 6  # Base case for the first row
        
        # Build solutions row by row
        for i in range(2, n + 1):
            # New ABC patterns can come from:
            # 3 choices from previous ABC + 2 choices from previous ABA
            new_x = (3 * x + 2 * y) % MOD
            
            # New ABA patterns can come from:
            # 2 choices from previous ABC + 2 choices from previous ABA
            new_y = (2 * x + 2 * y) % MOD
            
            x, y = new_x, new_y
        
        # Total ways is sum of both patterns
        return (x + y) % MOD
