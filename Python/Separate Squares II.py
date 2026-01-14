# https://leetcode.com/problems/separate-squares-ii/

# Example 1:
# Input: squares = [[0,0,1],[2,2,1]]
# Output: 1.00000
# Explanation:
# Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []

        # Create sweep-line events: +1 for start of square, -1 for end of square
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()

        xs = []                # active x-intervals
        prev_y = events[0][0]  # previous sweep y
        total = 0              # total covered area
        areas = []             # list of (y_start, height, width)

        # Computes total union length of overlapping x-intervals
        def union_len(intervals):
            intervals.sort()
            res = 0
            end = -10**30

            for a, b in intervals:
                if a > end:
                    res += b - a
                    end = b
                elif b > end:
                    res += b - end
                    end = b

            return res

        # Sweep line over y-axis
        for y, typ, x1, x2 in events:
            if y > prev_y and xs:
                h = y - prev_y
                w = union_len(xs)
                areas.append((prev_y, h, w))
                total += h * w

            if typ == 1:
                xs.append((x1, x2))     # add interval
            else:
                xs.remove((x1, x2))     # remove interval

            prev_y = y

        # Find horizontal line that splits total area into half
        half = total / 2
        acc = 0

        for y, h, w in areas:
            if acc + h * w >= half:
                return y + (half - acc) / w
            acc += h * w

        return 0.0
