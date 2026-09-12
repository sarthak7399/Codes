# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

# Example 1:
# Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
# Output: [2,3]
# Explanation:
# You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

import bisect
from typing import List

class Solution:
    def maximumWeight(self, I: List[List[int]]) -> List[int]:
        # Sort intervals by their start time.
        # Store each interval as:
        # (start, end, weight, original_index)
        A = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(I)
        )

        # Store all interval start times separately for binary search.
        S = [x[0] for x in A]

        # Number of intervals.
        n = len(A)

        # dp[i][k] stores:
        # (maximum total weight, tuple of original interval indices)
        #
        # considering intervals from index i onwards and selecting
        # at most k non-overlapping intervals.
        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        # Process intervals from right to left.
        for i in range(n - 1, -1, -1):
            l, r, w, id = A[i]

            # Find the first interval whose start time is strictly
            # greater than the current interval's end time.
            #
            # This gives the next non-overlapping interval.
            nxt = bisect.bisect_right(S, r)

            # Try selecting up to 1, 2, 3, or 4 intervals.
            for k in range(1, 5):

                # Option 1: Skip the current interval.
                bw, bids = dp[i + 1][k]

                # Option 2: Take the current interval and continue
                # from the next non-overlapping interval.
                pw, pids = dp[nxt][k - 1]

                # Calculate the total weight after taking it.
                tw = pw + w

                # Keep the selected original indices sorted.
                tids = tuple(sorted(pids + (id,)))

                # Choose the option with the greater total weight.
                #
                # If both have the same weight, choose the
                # lexicographically smaller list of indices.
                dp[i][k] = (
                    (tw, tids)
                    if tw > bw or (
                        tw == bw and
                        (not bids or tids < bids)
                    )
                    else (bw, bids)
                )

        # Return the indices of the maximum-weight selection
        # using at most four non-overlapping intervals.
        return list(dp[0][4][1])