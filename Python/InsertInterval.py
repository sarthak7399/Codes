# https://leetcode.com/problems/insert-interval/description/?envType=daily-question&envId=2024-03-15

# Note that you don't need to modify intervals in-place. You can make a new array and return it.
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []  # Initialize an empty list to store the merged intervals
        i = 0  # Initialize a pointer for iterating through the intervals list

        while i < len(intervals) and intervals[i][1] < newInterval[0]:      # Iterate through the intervals list until the end or until the end of an interval is less than the start of the newInterval
            merged.append(intervals[i])  # Add intervals that do not overlap with the newInterval directly to the merged list
            i += 1
               
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:      # Iterate through the intervals list until the end or until the start of an interval is less than or equal to the end of the newInterval
            # Update the newInterval to merge with the current interval by taking the minimum of the start values and the maximum of the end values
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)  # Add the merged newInterval to the merged list
        
        while i < len(intervals):       # Iterate through the remaining intervals in the intervals list and append them directly to the merged list
            merged.append(intervals[i])
            i += 1
        
        return merged  