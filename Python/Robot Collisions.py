# https://leetcode.com/problems/robot-collisions/submissions/1319939784/?envType=daily-question&envId=2024-07-13

# Example 1:
# Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
# Output: [2,17,9,15,10]
# Explanation: No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].

from typing import List
class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        surviving_robots = []
        for index in sorted(range(len(positions)), key=lambda i: positions[i]):
            if not surviving_robots:
                surviving_robots.append(index)
            else:
                new_robot_removed = False
                while (
                    surviving_robots
                    and directions[surviving_robots[-1]] == "R"
                    and directions[index] == "L"
                ):
                    if healths[surviving_robots[-1]] == healths[index]:
                        surviving_robots.pop()
                        new_robot_removed = True
                        break
                    if healths[surviving_robots[-1]] > healths[index]:
                        healths[surviving_robots[-1]] -= 1
                        new_robot_removed = True
                        break
                    surviving_robots.pop()
                    healths[index] -= 1
                if not new_robot_removed:
                    surviving_robots.append(index)

        surviving_robots.sort()
        return [healths[index] for index in surviving_robots]