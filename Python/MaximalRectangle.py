# https://leetcode.com/problems/maximal-rectangle/description/

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Get the number of rows and columns in the matrix
        r, c = len(matrix), len(matrix[0])
        
        # Base case: if the matrix has only one element
        if r == 1 and c == 1:
            if matrix[0][0] == '1':
                return 1
            else:
                return 0
        
        # Initialize a height array with all zeros
        h = [0] * (c + 1)
        
        # Initialize the maximum area to 0
        maxArea = 0

        # Iterate through each row in the matrix
        for i, row in enumerate(matrix):
            st = [-1]  # Initialize a stack with -1
            row.append('0')  # Add a dummy column with '0'
            
            # Iterate through each column in the row
            for j, x in enumerate(row):
                # Build the height array
                if x == '1':
                    h[j] += 1
                else:
                    h[j] = 0
                
                # Maintain a monotonic stack with at least one element -1
                while len(st) > 1 and (j == c or h[j] < h[st[-1]]):
                    m = st[-1]
                    st.pop()
                    w = j - st[-1] - 1
                    area = h[m] * w
                    maxArea = max(maxArea, area)
                st.append(j)
        
        return maxArea  # Return the maximum area

        