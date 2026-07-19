# https://leetcode.com/problems/walking-robot-simulation/


# Example 1:
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 3 units to (3, 4).
# The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.

from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        # Convert obstacles list into a set of tuples for O(1) lookup
        obstacles = set(tuple(_) for _ in obstacles)
        
        # res → maximum squared distance from origin
        # (curX, curY) → current position of robot
        # (diffX, diffY) → current direction vector
        # Initially facing north → (0, 1)
        res, curX, curY, diffX, diffY = 0, 0, 0, 0, 1

        # Process each command
        for command in commands:

            # -------- Case 1: Direction change --------
            if command < 0:
                
                # Use match-case for cleaner direction handling
                match command:
                    
                    case -1:
                        # Turn right (clockwise)
                        # (dx, dy) → (dy, -dx)
                        diffX, diffY = diffY, -diffX
                    
                    case -2:
                        # Turn left (anti-clockwise)
                        # (dx, dy) → (-dy, dx)
                        diffX, diffY = -diffY, diffX
                
                continue  # Skip movement logic

            # -------- Case 2: Move forward --------
            # Move step by step to handle obstacles
            for _ in range(command):

                # Next position
                nextX, nextY = curX + diffX, curY + diffY

                # If obstacle encountered → stop moving further
                if (nextX, nextY) in obstacles:
                    break

                # Otherwise, update position
                curX, curY = nextX, nextY

            # Update maximum distance from origin (squared distance)
            res = max(res, curX * curX + curY * curY)

        # Return the maximum distance achieved
        return res