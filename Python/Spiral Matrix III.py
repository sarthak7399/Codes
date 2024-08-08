# https://leetcode.com/problems/spiral-matrix-iii/

# Example 1:
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]

from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        output = [[rStart,cStart]]
        r = rStart
        c = cStart
        total = rows * cols
        i = 1
        count = 1
        while True:
            #dn = ['e','s','w','n']
            # move to east
            for _ in range(i):
                c += 1
                if r>=0 and r<rows and c>=0 and c<cols:
                    output.append([r,c])
                    count += 1
            if count==total:
                break

            # move to south
            for _ in range(i):
                r += 1
                if r>=0 and r<rows and c>=0 and c<cols:
                    output.append([r,c])
                    count += 1
            if count==total:
                break

            # move to west
            for _ in range(i+1):
                c -= 1
                if r>=0 and r<rows and c>=0 and c<cols:
                    output.append([r,c])
                    count += 1
            if count==total:
                break

            # move to north
            for _ in range(i+1):
                r -= 1
                if r>=0 and r<rows and c>=0 and c<cols:
                    output.append([r,c])
                    count += 1
            if count==total:
                break

            i += 2
        return output
        