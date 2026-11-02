# https://leetcode.com/problems/image-overlap/

# Example 1:
# Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
# Output: 3
# Explanation: We translate img1 to right by 1 unit and down by 1 unit.
# The number of positions that have a 1 in both images is 3 (shown in red).

from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # Get the size of the square images.
        n = len(img1)

        # Store coordinates of all 1s in img1.
        A = [
            (i, j)
            for i in range(n)
            for j in range(n)
            if img1[i][j] == 1
        ]

        # Store coordinates of all 1s in img2.
        B = [
            (i, j)
            for i in range(n)
            for j in range(n)
            if img2[i][j] == 1
        ]

        # cnt[dx][dy] counts how many pairs of 1s have the same
        # relative displacement between img1 and img2.
        #
        # Offset by n so that negative displacement values can
        # also be used as valid array indices.
        cnt = [[0] * (2 * n) for _ in range(2 * n)]

        # Store the maximum number of overlapping 1s found so far.
        best = 0

        # Try every 1-coordinate from img1.
        for ax, ay in A:

            # Match it with every 1-coordinate from img2.
            for bx, by in B:

                # Calculate the relative shift required to align
                # (ax, ay) from img1 with (bx, by) from img2.
                #
                # Adding n handles negative shift values.
                dx = bx - ax + n
                dy = by - ay + n

                # Increment the count for this particular shift.
                cnt[dx][dy] += 1

                # The shift with the highest count gives the
                # maximum number of overlapping 1s.
                best = max(best, cnt[dx][dy])

        # Return the maximum overlap for any possible shift.
        return best