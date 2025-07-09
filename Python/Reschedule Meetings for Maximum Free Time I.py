# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

# Example 1:
# Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]
# Output: 2
# Explanation:
# Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)     # Total number of events
        busy = 0               # Total time occupied by the first k events

        # Step 1: Calculate initial busy time for the first k events
        for i in range(k):
            busy += endTime[i] - startTime[i]

        # Step 2: If we must attend all events, free time is eventTime minus total busy time
        if n == k:
            return eventTime - busy

        # Step 3: Initial answer: free time before the next event after first k
        ans = startTime[k] - busy

        l = 0  # Left pointer of the sliding window
        for r in range(k, n):
            # Step 4: Slide window: add new event duration and remove oldest event duration
            busy += (endTime[r] - startTime[r]) - (endTime[l] - startTime[l])

            # Step 5: Compute the next end boundary (either eventTime or start of next event)
            end = eventTime if r == n - 1 else startTime[r + 1]
            start = endTime[l]  # Start boundary is the end of the leftmost event in the window

            # Step 6: Update maximum free time
            ans = max(ans, end - start - busy)

            l += 1  # Move left pointer forward

        return ans
