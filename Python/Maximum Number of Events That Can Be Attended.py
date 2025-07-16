# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

# Example 1:
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.

from heapq import heappush, heappop
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day
        events.sort()

        # Find the latest possible day from all events
        total = max(event[1] for event in events)

        pq = []  # Min-heap to store event end days (active events)
        i = 0    # Pointer to traverse the sorted events
        day = 1  # Current day
        cnt = 0  # Count of events attended

        while day <= total:
            # If no active events, fast-forward to the next available event start day
            if not pq and i < len(events):
                day = max(day, events[i][0])

            # Remove events that have already expired (end day < today)
            while pq and pq[0] < day:
                heappop(pq)

            # Add all events that start today into the heap
            while i < len(events) and events[i][0] == day:
                heappush(pq, events[i][1])
                i += 1

            # Attend the event that ends earliest (greedy strategy)
            if pq:
                heappop(pq)
                cnt += 1
            elif i == len(events):  # If no more events left to process, stop early
                break

            # Move to the next day
            day += 1

        return cnt
