# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

# Example 1:
# Input: mountainHeight = 4, workerTimes = [2,1,1]
# Output: 3
# Explanation:
# One way the height of the mountain can be reduced to 0 is:
# Worker 0 reduces the height by 1, taking workerTimes[0] = 2 seconds.
# Worker 1 reduces the height by 2, taking workerTimes[1] + workerTimes[1] * 2 = 3 seconds.
# Worker 2 reduces the height by 1, taking workerTimes[2] = 1 second.
# Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3 seconds.

import heapq

class Solution:
    def minNumberOfSeconds(self, h, t):
        
        # Priority queue (min heap)
        # Each element: (next_available_time, worker_index, tasks_done_by_worker)
        pq = []

        # Initialize the heap with the first task for each worker
        for i in range(len(t)):
            # First task time = t[i]
            # Worker has completed 1 task
            heapq.heappush(pq, (t[i], i, 1))

        # This will store the latest finishing time
        res = 0

        # Continue assigning tasks until h tasks are completed
        while h > 0:

            # Get the worker who will finish the next task earliest
            tm, idx, x = heapq.heappop(pq)

            # Update result with the finishing time of this task
            res = tm

            # One task completed
            h -= 1

            # If more tasks are remaining
            if h > 0:

                # Next task count for this worker
                nx = x + 1

                # Time required for worker to complete nx tasks
                # Using triangular number formula:
                # t[idx] * (1 + 2 + ... + nx)
                # = t[idx] * (nx * (nx + 1) / 2)
                nt = t[idx] * (nx * (nx + 1) // 2)

                # Push updated worker state back into heap
                heapq.heappush(pq, (nt, idx, nx))

        # Return the time when the last task finishes
        return res