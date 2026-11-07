# https://leetcode.com/problems/process-tasks-using-servers/

# Example 1:
# Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
# Output: [2,2,0,2,1,2]
# Explanation: Events in chronological order go as follows:
# - At second 0, task 0 is added and processed using server 2 until second 1.
# - At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
# - At second 2, task 2 is added and processed using server 0 until second 5.
# - At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
# - At second 4, task 4 is added and processed using server 1 until second 5.
# - At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        import heapq

        # Min-heap of available servers, ordered by (weight, index).
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        # Min-heap of busy servers, ordered by (finish_time, weight, index).
        busy = []

        # Store the server assigned to each task.
        ans = [0] * len(tasks)

        # Process tasks in their given order.
        for j, t in enumerate(tasks):

            # Move all servers that have completed their tasks
            # back into the available server heap.
            while busy and busy[0][0] <= j:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            # If an available server exists, choose the one with
            # the smallest weight, breaking ties by index.
            if free:
                w, i = heapq.heappop(free)
                ans[j] = i

                # Mark the server as busy until time j + t.
                heapq.heappush(busy, (j + t, w, i))

            else:
                # If no server is available, select the server
                # that will finish its current task earliest.
                # Ties are resolved by weight and then index.
                ft, w, i = heapq.heappop(busy)
                ans[j] = i

                # Assign the current task immediately after the
                # server finishes its existing task.
                heapq.heappush(busy, (ft + t, w, i))

        # Return the server indices assigned to all tasks.
        return ans