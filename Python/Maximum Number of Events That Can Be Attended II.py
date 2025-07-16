# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

# Example 1:
# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.

from bisect import bisect_right
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Step 1: Sort events by their start day
        events.sort(key=lambda e: e[0])

        # Step 2: Precompute a list of just the start days for binary search
        starts = [e[0] for e in events]
        n = len(events)

        # Step 3: For each event, find the next non-overlapping event index using binary search
        next_idx = [0] * n
        for i in range(n):
            end_i = events[i][1]
            # Find the index of the first event that starts after the current one ends
            next_idx[i] = bisect_right(starts, end_i)

        # Step 4: Base case: store the best single-event result from i to end
        prev = [0] * (n + 1)  # prev[i] = max value using 1 event from i to end
        for i in range(n - 1, -1, -1):
            prev[i] = max(prev[i + 1], events[i][2])  # max between skipping or taking current event

        res = prev[0]  # Initialize result with best single-event choice

        # Step 5: For k > 1, use dynamic programming to build up optimal values
        for _ in range(2, k + 1):  # For 2 to k events
            curr = [0] * (n + 1)  # curr[i] = max value using _ events from i to end
            for i in range(n - 1, -1, -1):
                take = events[i][2]  # Value if we take this event
                j = next_idx[i]      # Next non-overlapping event index
                if j <= n:
                    take += prev[j]  # Add best value from next valid event chain
                curr[i] = max(curr[i + 1], take)  # Max of skipping or taking this event
            res = max(res, curr[0])  # Update overall max
            prev = curr  # Move to next iteration

        return res
