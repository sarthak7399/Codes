# https://leetcode.com/problems/zero-array-transformation-iii/

# Example 1:
# Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
# Output: 1
# Explanation:
# After removing queries[2], nums can still be converted to a zero array.
# Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
# Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.

import heapq

class Solution:
    def maxRemoval(self, nums, queries):
        n = len(nums)
        m = len(queries)

        # `workload[i]` tracks the net increment of workload at time `i`.
        # It will be prefix summed later to get actual workload at each time.
        workload = [0] * (n + 1)

        # Sort queries by their start time
        queries.sort()

        available = []  # Max heap (using negated values for max behavior)
        q_index = 0  # Pointer to iterate through sorted queries

        # Iterate over each time unit (0 to n-1)
        for time in range(n):
            # Prefix sum to accumulate active workloads at current time
            if time > 0:
                workload[time] += workload[time - 1]

            # Push all queries that start at the current `time` into the heap
            while q_index < m and queries[q_index][0] == time:
                # Push the end time as negative to simulate a max-heap
                heapq.heappush(available, -queries[q_index][1])
                q_index += 1

            # Assign work at this time until `nums[time]` is satisfied
            while workload[time] < nums[time]:
                # If no query is available or the best one has already expired
                if not available or -available[0] < time:
                    return -1  # Impossible to satisfy workload

                # Use the current best available query
                workload[time] += 1
                end_time = -heapq.heappop(available)

                # Remove 1 unit of workload after the end time of the query
                if end_time + 1 < len(workload):
                    workload[end_time + 1] -= 1

        # Remaining queries that were never used
        return len(available)
