# https://leetcode.com/problems/robot-return-to-origin/

# Example 1:
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        # pos[0] → x-coordinate (left/right)
        # pos[1] → y-coordinate (up/down)
        pos = [0, 0]

        # Traverse each move
        for ch in moves:

            if ch == 'U':
                # Move up → increase y
                pos[1] += 1

            elif ch == 'D':
                # Move down → decrease y
                pos[1] -= 1

            elif ch == 'R':
                # Move right → increase x
                pos[0] += 1

            else:
                # Move left → decrease x
                pos[0] -= 1

        # Check if we returned to origin (0, 0)
        if pos == [0, 0]:
            return True
        else:
            return False