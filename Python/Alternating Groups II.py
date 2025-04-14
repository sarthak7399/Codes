# https://leetcode.com/problems/alternating-groups-ii/

# Example 1:
# Input: colors = [0,1,0,1,0], k = 3
# Output: 3

class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        w = 1  # Tracks the length of the current alternating sequence
        ans = 0  # Stores the count of valid alternating groups
        n = len(colors)  # Length of the input array

        # Iterate over the array in a circular manner (with `k-2` additional iterations)
        for i in range(1, n + k - 2 + 1):
            # Check if the current color is different from the previous one (alternating pattern)
            if colors[i % n] != colors[(i - 1 + n) % n]:
                w += 1  # Increase the length of the current alternating sequence
            else:
                w = 1  # Reset sequence length if the pattern breaks

            # If the current sequence length is at least `k`, count it as a valid group
            if w >= k:
                ans += 1  

        return ans  # Return the total count of alternating groups
