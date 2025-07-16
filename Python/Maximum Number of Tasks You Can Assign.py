# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

# Example 1:
# Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# Output: 3
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 2 (0 + 1 >= 1)
# - Assign worker 1 to task 1 (3 >= 2)
# - Assign worker 2 to task 0 (3 >= 3)

from collections import deque

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        # Sort tasks and workers in ascending order
        tasks.sort()
        workers.sort()

        # Helper function to check if we can assign 'mid' number of tasks
        def can_assign(mid):
            # Queue to hold workers who are assigned a pill (boosted strength)
            boosted = deque()
            # Start from the strongest available worker
            w = len(workers) - 1
            # Remaining pills
            free_pills = pills

            # Go through the 'mid' hardest tasks (rightmost in sorted array)
            for t in reversed(tasks[:mid]):
                # Case 1: A previously boosted worker can handle the task
                if boosted and boosted[0] >= t:
                    boosted.popleft()
                # Case 2: A strong enough unboosted worker is available
                elif w >= 0 and workers[w] >= t:
                    w -= 1
                else:
                    # Case 3: Try boosting a weaker worker
                    while w >= 0 and workers[w] + strength >= t:
                        boosted.append(workers[w])
                        w -= 1
                    # No boosted worker available or no pills left
                    if not boosted or free_pills == 0:
                        return False
                    # Use a pill on a worker
                    boosted.pop()
                    free_pills -= 1

            return True  # All tasks successfully assigned

        # Binary search to find the maximum number of assignable tasks
        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            mid = (low + high + 1) // 2  # Try the upper half first
            if can_assign(mid):
                low = mid  # Try more tasks
            else:
                high = mid - 1  # Try fewer tasks

        return low  # Maximum number of tasks that can be assigned
