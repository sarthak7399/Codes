# https://leetcode.com/problems/set-intersection-size-at-least-two/

# Example 1:
# Input: intervals = [[1,3],[3,7],[8,9]]
# Output: 5
# Explanation: let nums = [2, 3, 4, 8, 9].
# It can be shown that there cannot be any containing array of size 4.

import heapq

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals by ending point to ensure greedy selection works
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])

        # Start with the last two elements of the first interval
        prev1 = intervals[0][1] - 1
        prev2 = intervals[0][1]
        c = 2  # Minimum two points needed

        # Process remaining intervals
        for i in range(1, n):
            start, end = intervals[i]

            # If the interval starts after both chosen points, add two new points
            if prev2 < start:
                prev1 = end - 1
                prev2 = end
                c += 2

            # If the interval overlaps only one chosen point, add one more
            elif prev1 < start:
                if end == prev2:
                    prev1 = end - 1
                else:
                    prev1 = end

                # Ensure prev1 < prev2 ordering
                prev1, prev2 = min(prev1, prev2), max(prev1, prev2)
                c += 1

        return c
