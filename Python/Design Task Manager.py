# https://leetcode.com/problems/design-task-manager/

# Example 1:
# Input:
# ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
# [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
# Output:
# [null, null, null, 3, null, null, 5]
# Explanation
# TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.
# taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
# taskManager.edit(102, 8); // Updates priority of task 102 to 8.
# taskManager.execTop(); // return 3. Executes task 103 for User 3.
# taskManager.rmv(101); // Removes task 101 from the system.
# taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
# taskManager.execTop(); // return 5. Executes task 105 for User 5.

from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # Maps taskId -> priority
        self.task_prio_map = defaultdict(int)
        # Maps taskId -> userId
        self.task_user_map = defaultdict(int)
        # Max-heap (simulated using min-heap with negative values)
        self.t_hq = []

        # Initialize with given tasks
        for task in tasks:
            u, t, p = task
            self.task_prio_map[t] = p
            self.task_user_map[t] = u
            heappush(self.t_hq, (-p, -t))   # push (-priority, -taskId) for max behavior

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # Add new task
        self.task_prio_map[taskId] = priority
        self.task_user_map[taskId] = userId
        heappush(self.t_hq, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        # Update priority in map
        self.task_prio_map[taskId] = newPriority
        # Old entries in heap become stale (lazy deletion)
        heappush(self.t_hq, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        # Mark task as deleted by setting priority = -1
        # Stale entries remain in heap and will be ignored during execTop
        self.task_prio_map[taskId] = -1

    def execTop(self) -> int:
        while True:
            if not self.t_hq:
                # No valid tasks left
                return -1
            pt = heappop(self.t_hq)
            p, t = -pt[0], -pt[1]
            # Check if current heap entry matches the "latest" priority
            if self.task_prio_map[t] == p:
                break
        # Mark executed task as removed
        self.task_prio_map[t] = -1
        return self.task_user_map[t]
