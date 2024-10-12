# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

# Example 1:
# Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# Output: 3
# Explanation: We can divide the intervals into the following groups:
# - Group 1: [1, 5], [6, 8].
# - Group 2: [2, 3], [5, 10].
# - Group 3: [1, 10].
# It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        end_ptr, group_count = 0, 0

        for start in start_times:
            if start > end_times[end_ptr]:
                end_ptr += 1
            else:
                group_count += 1

        return group_count