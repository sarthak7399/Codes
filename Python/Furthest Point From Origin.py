# https://leetcode.com/problems/furthest-point-from-origin/

# Example 1:
# Input: moves = "L_RL__R"
# Output: 3
# Explanation: The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = r = d = 0  # l → count of 'L', r → count of 'R', d → count of '_' (unknown)

        # Count occurrences of each type of move
        for c in moves:
            if c == 'L':
                l += 1
            elif c == 'R':
                r += 1
            else:
                d += 1  # '_' can be treated as either L or R

        # Max distance is achieved by assigning all '_' in the direction
        # that increases the imbalance between L and R
        return abs(l - r) + d