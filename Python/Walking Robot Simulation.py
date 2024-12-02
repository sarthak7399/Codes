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
        obstacles = set(tuple(_) for _ in obstacles)
        res, curX, curY, diffX, diffY  = 0, 0, 0, 0, 1

        for command in commands:
            if command < 0: #change direction 
                match command:
                    case -1: diffX, diffY = diffY, -diffX # clockwise
                    case -2: diffX, diffY = -diffY, diffX # anti-clockwise
                continue
            
            for _ in range(command):
                nextX, nextY = curX + diffX, curY + diffY
                if (nextX, nextY) in obstacles: break
                curX, curY = nextX, nextY
            
            res = max(res, curX*curX + curY*curY)

        return res