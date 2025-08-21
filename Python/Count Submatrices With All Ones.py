# https://leetcode.com/problems/count-submatrices-with-all-ones/

# Example 1:
# Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
# Output: 13
# Explanation: 
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])   # number of rows and columns
        h = [0] * c                    # height array → stores consecutive 1s in each column
        ans = 0                        # total number of submatrices filled with 1s

        # Iterate through each row
        for i in range(r):
            # Update the histogram heights for this row
            for j in range(c):
                # If current cell is 1, increase height; else reset to 0
                h[j] = h[j] + 1 if mat[i][j] else 0

            # sumv[j] → number of submatrices ending at column j in current row
            sumv, st = [0] * c, []     # st = monotonic stack to maintain increasing heights

            # Process histogram like "largest rectangle in histogram" approach
            for j in range(c):
                # Maintain increasing stack of column heights
                while st and h[st[-1]] >= h[j]:
                    st.pop()

                if st:  
                    # If there's a smaller bar to the left
                    p = st[-1]
                    # Extend submatrices ending at j using previous sumv[p]
                    sumv[j] = sumv[p] + h[j] * (j - p)
                else:
                    # No smaller bar on left → all submatrices use current height
                    sumv[j] = h[j] * (j + 1)

                # Push current index to stack
                st.append(j)

                # Accumulate the count of submatrices
                ans += sumv[j]

        return ans
