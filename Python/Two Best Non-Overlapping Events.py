# https://leetcode.com/problems/two-best-non-overlapping-events/

# Example 1:
# Input: events = [[1,3,2],[4,5,2],[2,4,3]]
# Output: 4
# Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        # Create timeline with start and end markers
        Time = [(0, 0, 0)] * (n * 2)

        for i, (s, e, v) in enumerate(events):
            Time[2 * i] = (s, False, v)   # Event start
            Time[2 * i + 1] = (e, True, v)  # Event end

        # Sort by time
        Time.sort()

        ans, maxV = 0, 0
        # Sweep through timeline
        for t, isEnd, v in Time:
            if isEnd:
                # Update best finished event value so far
                maxV = max(maxV, v)
            else:
                # Combine current event with best previous one
                ans = max(ans, maxV + v)

        return ans
