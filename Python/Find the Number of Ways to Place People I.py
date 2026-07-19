# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

# Example 1:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 0
# Explanation:
# There is no way to choose A and B so A is on the upper left side of B.

class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        # Step 1: Sort points
        #   - By x-coordinate ascending
        #   - If x is same, by y-coordinate descending
        points.sort(key=lambda x: (x[0], -x[1]))
        
        n = len(points)
        result = 0

        # Step 2: Iterate over each point i as the "left" point
        for i in range(n):
            top = points[i][1]          # highest y allowed for a valid pair
            bot = float("-inf")         # lowest y allowed (dynamic)
            
            # Step 3: Compare with all points j to the right of i
            for j in range(i + 1, n):
                y = points[j][1]
                
                # Valid pair condition: y must be between (bot, top]
                if bot < y <= top:
                    result += 1          # found a valid pair
                    bot = y              # update lowest bound
                    if bot == top:       # can't go lower, stop early
                        break

        return result
