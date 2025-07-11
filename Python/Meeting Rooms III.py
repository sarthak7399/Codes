# https://leetcode.com/problems/meeting-rooms-iii/

# Example 1:
# Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
# Output: 0
# Explanation:
# - At time 0, both rooms are not being used. The first meeting starts in room 0.
# - At time 1, only room 1 is not being used. The second meeting starts in room 1.
# - At time 2, both rooms are being used. The third meeting is delayed.
# - At time 3, both rooms are being used. The fourth meeting is delayed.
# - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
# - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
# Both rooms 0 and 1 held 2 meetings, so we return 0. 

import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Step 1: Sort meetings by start time
        meetings.sort()

        # Step 2: Min-heap for available rooms (lowest room number)
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        # Step 3: Min-heap for busy rooms: (end time, room number)
        busy = []
        count = [0] * n  # Step 4: Count meetings per room

        # Step 5: Process each meeting
        for start, end in meetings:
            duration = end - start

            # Free rooms that have finished by current meeting start time
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                # Assign meeting to the smallest free room
                room = heapq.heappop(free_rooms)
                count[room] += 1
                heapq.heappush(busy, (end, room))
            else:
                # Delay the meeting until a room is free
                free_time, room = heapq.heappop(busy)
                count[room] += 1
                heapq.heappush(busy, (free_time + duration, room))

        # Step 6: Find room with most meetings
        max_meetings = max(count)
        for i, c in enumerate(count):
            if c == max_meetings:
                return i