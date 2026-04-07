# https://leetcode.com/problems/walking-robot-simulation-ii/

# Example 1:
# Input:
# ["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
# [[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
# Output:
# [null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]
# Explanation:
# Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
# robot.step(2);  // It moves two steps East to (2, 0), and faces East.
# robot.step(2);  // It moves two steps East to (4, 0), and faces East.
# robot.getPos(); // return [4, 0]
# robot.getDir(); // return "East"
# robot.step(2);  // It moves one step East to (5, 0), and faces East.
#                 // Moving the next step East would be out of bounds, so it turns and faces North.
#                 // Then, it moves one step North to (5, 1), and faces North.
# robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
# robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
#                 // Then, it moves four steps West to (1, 2), and faces West.
# robot.getPos(); // return [1, 2]
# robot.getDir(); // return "West"

from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        # Grid dimensions
        self.w = width
        self.h = height

        # Current position (start at bottom-left corner)
        self.x = 0
        self.y = 0

        # Direction:
        # 0 = East, 1 = North, 2 = West, 3 = South
        self.dir = 0

        # Perimeter length (total steps to complete one full cycle)
        # Subtract 4 to avoid counting corners twice
        self.per = 2 * (self.w + self.h) - 4

    def step(self, num: int) -> None:
        
        # If perimeter is 0 (edge case: 1x1 grid), no movement possible
        if self.per == 0:
            return

        # Reduce steps using modulo (full cycles don't change position)
        num %= self.per

        # -------- Special Case: Full cycle --------
        # If num becomes 0 after modulo:
        # Robot completes a full loop and returns to same position
        if num == 0:
            if self.x == 0 and self.y == 0:
                # At origin, direction should be South after full cycle
                self.dir = 3
            return

        # -------- Move step-by-step along boundary --------
        while num > 0:

            if self.dir == 0:  # Moving East (→)
                
                # Max steps possible before hitting right boundary
                move = min(num, self.w - 1 - self.x)
                
                self.x += move
                num -= move

                # If steps still remain → turn North
                if num > 0:
                    self.dir = 1

            elif self.dir == 1:  # Moving North (↑)
                
                # Max steps before hitting top boundary
                move = min(num, self.h - 1 - self.y)
                
                self.y += move
                num -= move

                # Turn West
                if num > 0:
                    self.dir = 2

            elif self.dir == 2:  # Moving West (←)
                
                # Max steps before hitting left boundary
                move = min(num, self.x)
                
                self.x -= move
                num -= move

                # Turn South
                if num > 0:
                    self.dir = 3

            else:  # Moving South (↓)
                
                # Max steps before hitting bottom boundary
                move = min(num, self.y)
                
                self.y -= move
                num -= move

                # Turn East
                if num > 0:
                    self.dir = 0

    def getPos(self) -> List[int]:
        # Return current position
        return [self.x, self.y]

    def getDir(self) -> str:
        # Convert direction integer to string
        if self.dir == 0:
            return "East"
        elif self.dir == 1:
            return "North"
        elif self.dir == 2:
            return "West"
        else:
            return "South"