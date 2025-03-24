# https://leetcode.com/problems/count-days-without-meetings/

# Example 1:
# Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
# Output: 2
# Explanation:
# There is no meeting scheduled on the 4th and 8th days.

from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        # Sort meetings by start day
        meetings.sort()
        
        # Merge overlapping meetings
        merged_meetings = []
        for meeting in meetings:
            if not merged_meetings or meeting[0] > merged_meetings[-1][1]:  
                # No overlap, add new meeting
                merged_meetings.append(meeting)
            else:
                # Merge overlapping meetings
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])
        
        # Count total meeting days
        meeting_days_count = 0
        for start, end in merged_meetings:
            meeting_days_count += end - start + 1
        
        # Subtract meeting days from total days
        return days - meeting_days_count
