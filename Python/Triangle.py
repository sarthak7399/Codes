# https://leetcode.com/problems/triangle/

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        n = len(t)
        # Start from row 1, update each element in-place
        for i in range(1, n):
            # First element in row i can only come from t[i-1][0]
            t[i][0] += t[i-1][0]

            # Last element in row i can only come from t[i-1][i-1]
            t[i][i] += t[i-1][i-1]

            # For middle elements, take min from two possible parents
            for j in range(1, i):
                t[i][j] += min(t[i-1][j], t[i-1][j-1])

        # Answer is minimum in the last row
        return min(t[-1])
