# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

# Example 1:
# Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
# Output: 1
# Explanation: We start from index 1 and can reach "hello" by
# - moving 3 units to the right to reach index 4.
# - moving 2 units to the left to reach index 4.
# - moving 4 units to the right to reach index 0.
# - moving 1 unit to the left to reach index 0.
# The shortest distance to reach "hello" is 1.

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)  # Total number of words

        # Maximum distance needed is half the array (circular traversal)
        n2 = n // 2 + 1

        # Try increasing distances from startIndex
        for d in range(n2):

            # Move left in circular manner
            # If index goes negative, wrap around using (n + index)
            l = startIndex - d if startIndex >= d else n + startIndex - d

            # Move right in circular manner
            # If index exceeds n, wrap around using (index - n)
            r = startIndex + d - n if startIndex + d >= n else startIndex + d

            # Check if either left or right position matches target
            if words[l] == target or words[r] == target:
                return d  # Minimum distance found

        # If target not found in circular traversal
        return -1