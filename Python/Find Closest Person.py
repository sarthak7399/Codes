# https://leetcode.com/problems/find-closest-person/

# Example 1:
# Input: x = 2, y = 7, z = 4
# Output: 1
# Explanation:
# Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
# Person 2 is at position 7 and can reach Person 3 in 3 steps.
# Since Person 1 reaches Person 3 first, the output is 1.

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Compute absolute difference between x and z
        d1 = abs(x - z)
        # Compute absolute difference between y and z
        d2 = abs(y - z)

        # If x is closer to z than y → return 1
        if d1 < d2:
            return 1
        # If y is closer to z than x → return 2
        if d2 < d1:
            return 2
        # If both distances are equal → return 0
        return 0
