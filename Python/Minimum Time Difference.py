# https://leetcode.com/problems/minimum-time-difference/

# Example 1:
# Input: timePoints = ["23:59","00:00"]
# Output: 1

from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert each time in 'HH:MM' format into minutes since midnight
        minutes_list = []
        for time in timePoints:
            hours = int(time[:2])  # Extract hours
            minutes = int(time[3:])  # Extract minutes
            total_minutes = hours * 60 + minutes  # Convert time to total minutes
            minutes_list.append(total_minutes)

        # Sort the list of minutes
        minutes_list.sort()
        n = len(minutes_list)

        # Initialize the minimum time difference as the difference between the first and last time (across midnight)
        min_diff = 1440 + minutes_list[0] - minutes_list[n - 1]  # 1440 = total minutes in a day

        # Check for the minimum difference between consecutive times
        for i in range(1, n):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])

        return min_diff
