# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

# Example 1:
# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        # Size of the matrix (n x n)
        n = len(mat)

        # Bitmask to track which rotations are still valid
        # 0b1111 → all 4 rotations possible initially
        # Bit positions represent:
        # 1st bit (LSB)   → 90°
        # 2nd bit         → 180°
        # 3rd bit         → 270°
        # 4th bit (MSB)   → 0° (no rotation)
        m = 0b1111

        # Traverse every cell
        for i in range(n):
            for j in range(n):

                # Check 0° rotation (no rotation)
                # If mismatch → eliminate this possibility
                if mat[i][j] != target[i][j]:
                    m &= 0b1110   # turn off last bit

                # Check 90° rotation
                # (i, j) → (j, n-1-i)
                if mat[i][j] != target[j][n - 1 - i]:
                    m &= 0b1101   # turn off 2nd bit

                # Check 180° rotation
                # (i, j) → (n-1-i, n-1-j)
                if mat[i][j] != target[n - 1 - i][n - 1 - j]:
                    m &= 0b1011   # turn off 3rd bit

                # Check 270° rotation
                # (i, j) → (n-1-j, i)
                if mat[i][j] != target[n - 1 - j][i]:
                    m &= 0b0111   # turn off 4th bit

                # If all possibilities are eliminated → early exit
                if m == 0:
                    return False

        # If at least one rotation is still valid → return True
        return m != 0