# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

# Example 1:
# Input: tasks = [[1,2],[2,4],[4,8]]
# Output: 8
# Explanation:
# Starting with 8 energy, we finish the tasks in the following order:
#     - 3rd task. Now energy = 8 - 4 = 4.
#     - 2nd task. Now energy = 4 - 2 = 2.
#     - 1st task. Now energy = 2 - 1 = 1.
# Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.

from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        # Sort tasks by (minimum - actual) in descending order
        # Tasks requiring larger extra energy are done first
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        answer = 0  # Minimum initial energy required
        energy = 0  # Current available energy

        # Process each task
        for actual, minimum in tasks:

            # If current energy is less than required minimum
            if energy < minimum:

                # Add extra energy needed
                need = minimum - energy

                answer += need
                energy += need

            # Perform the task and reduce energy
            energy -= actual

        return answer