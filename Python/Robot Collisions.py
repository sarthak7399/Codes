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

        # Stack to keep indices of robots that are still alive
        surviving_robots = []

        # Process robots in order of their positions (left → right)
        for index in sorted(range(len(positions)), key=lambda i: positions[i]):

            # If no robots yet → simply add current robot
            if not surviving_robots:
                surviving_robots.append(index)
            else:
                new_robot_removed = False

                # Handle collision:
                # Only happens when previous robot is moving right (R)
                # and current robot is moving left (L)
                while (
                    surviving_robots
                    and directions[surviving_robots[-1]] == "R"
                    and directions[index] == "L"
                ):
                    # Compare healths of colliding robots

                    # Case 1: Equal health → both destroyed
                    if healths[surviving_robots[-1]] == healths[index]:
                        surviving_robots.pop()
                        new_robot_removed = True
                        break

                    # Case 2: Stack robot stronger → current robot destroyed
                    if healths[surviving_robots[-1]] > healths[index]:
                        healths[surviving_robots[-1]] -= 1  # lose 1 health
                        new_robot_removed = True
                        break

                    # Case 3: Current robot stronger → stack robot destroyed
                    surviving_robots.pop()
                    healths[index] -= 1  # lose 1 health
                    # Continue loop (current robot may collide again)

                # If current robot survives all collisions → add to stack
                if not new_robot_removed:
                    surviving_robots.append(index)

        # Sort surviving robots by original index order
        surviving_robots.sort()

        # Return their final healths
        return [healths[index] for index in surviving_robots]