# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

# Example 2:
# Input: colors = [1,8,3,8,3]
# Output: 4
# Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
# The furthest two houses with different colors are house 0 and house 4.
# House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)  # Total number of elements
        ans = 0          # Store maximum distance

        # Traverse the array
        for i in range(n):
            
            # If current color is different from the first color,
            # update distance from index 0 to i
            if colors[i] != colors[0]:
                ans = max(ans, i)

            # If current color is different from the last color,
            # update distance from index i to last index (n-1)
            if colors[i] != colors[-1]:
                ans = max(ans, n - 1 - i)

        return ans  # Return maximum distance found