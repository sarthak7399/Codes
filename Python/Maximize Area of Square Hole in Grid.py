# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

# Example 1:
# Input: n = 2, m = 1, hBars = [2,3], vBars = [2]
# Output: 4
# Explanation:
# The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4], and the vertical bars are [1,2,3].
# One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        # Finds maximum consecutive bars removed + 1 (gap size)
        def longest(a):
            a.sort()
            best = cur = 1

            for i in range(1, len(a)):
                if a[i] == a[i - 1] + 1:
                    cur += 1      # extend consecutive streak
                else:
                    cur = 1       # reset streak
                best = max(best, cur)

            return best + 1  # +1 gives actual hole size

        # Side of square is limited by both directions
        side = min(longest(hBars), longest(vBars))

        return side * side
