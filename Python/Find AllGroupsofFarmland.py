# https://leetcode.com/problems/find-all-groups-of-farmland/

# Example 1:
# Input: land = [[1,0,0],[0,1,1],[0,1,1]]
# Output: [[0,0,0,0],[1,1,2,2]]
# Explanation:
# The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
# The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].

from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        farmlands = []
        
        for i in range(rows):
            for j in range(cols):
                # check if (i, j) is the start of a new farmland rectangle
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    bottom_row = i
                    right_col = j

                    # expand down to find the bottom boundary 
                    while bottom_row + 1 < rows and land[bottom_row + 1][j] == 1:
                        bottom_row += 1
                    # expand right to find the right boundary 
                    while right_col + 1 < cols and land[i][right_col + 1] == 1:
                        right_col += 1

                    farmlands.append([i, j, bottom_row, right_col])
                    
        return farmlands