# https://leetcode.com/problems/remove-covered-intervals/

# Example 1:
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]):

        # Sort by:
        # 1. Starting point in ascending order.
        # 2. Ending point in descending order for equal starts.
        #
        # Example:
        # [[1,4], [1,3]] becomes [[1,4], [1,3]]
        # so that the larger interval comes first and
        # can cover the smaller one.
        intervals.sort(key=lambda x: (x[0], -x[1]))

        # Initially assume all intervals remain
        ans = len(intervals)

        # Track the current interval that may cover others
        low = intervals[0][0]
        high = intervals[0][1]

        # Traverse the remaining intervals
        for i in range(1, len(intervals)):

            # Current interval is covered if:
            # 1. It has the same starting point as the previous
            #    interval (the previous one must end later because
            #    of sorting), or
            # 2. Its ending point lies within the current maximum end.
            if intervals[i][0] == low or intervals[i][1] <= high:
                ans -= 1
            else:
                # This interval is not covered,
                # so make it the new reference interval.
                low = intervals[i][0]
                high = intervals[i][1]

        return ans