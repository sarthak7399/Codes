# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

# Example 1:
# Input: s = "NWSE", k = 1
# Output: 3
# Explanation:
# Change s[2] from 'S' to 'N'. The string s becomes "NWNE".
# Movement	Position (x, y)	Manhattan Distance	Maximum
# s[0] == 'N'	(0, 1)	0 + 1 = 1	1
# s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
# s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
# s[3] == 'E'	(0, 2)	0 + 2 = 2	3
# The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0  # Initialize coordinates (origin)
        distances = []  # Stores Manhattan distances from origin at each step

        # Simulate the path and record Manhattan distances
        for move in s:
            if move == "N":
                y += 1
            elif move == "S":
                y -= 1
            elif move == "E":
                x += 1
            elif move == "W":
                x -= 1
            # Manhattan distance from origin
            distances.append(abs(x) + abs(y))

        # If no reversals allowed, return the maximum distance directly
        if k == 0:
            return max(distances)

        max_dist = distances[1]  # Initialize max distance with second step
        previous = distances[0]  # Track previous distance to detect decreases
        added_boost = 0  # Total distance added by using reversals

        # Traverse through distances and apply up to k reversals
        for i in range(1, len(distances)):
            # If movement reduced the distance and reversals are available
            if distances[i] < previous and k > 0:
                added_boost += 2  # Reversing a move increases distance by 2
                k -= 1  # Use one reversal

            previous = distances[i]
            distances[i] += added_boost  # Apply accumulated boost
            max_dist = max(max_dist, distances[i])  # Track max distance

        return max_dist
