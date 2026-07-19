# https://leetcode.com/problems/decode-the-slanted-ciphertext/

# Example 1:
# Input: encodedText = "ch   ie   pr", rows = 3
# Output: "cipher"

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        # Edge case: no rows → nothing to decode
        if rows == 0:
            return ""

        # Total characters
        n = len(encodedText)

        # Edge case: empty string
        if n == 0:
            return ""

        # Number of columns
        # (encoded text is written row-wise into a matrix)
        cols = n // rows

        # -------- Step 1: Build matrix --------
        # Fill matrix row-wise using encodedText
        mat = []
        idx = 0

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(encodedText[idx])
                idx += 1
            mat.append(row)

        # -------- Step 2: Diagonal traversal --------
        # Traverse diagonals starting from first row (each column)
        result = []

        for startCol in range(cols):
            
            # Start from (0, startCol)
            i, j = 0, startCol

            # Move diagonally down-right
            while i < rows and j < cols:
                result.append(mat[i][j])
                i += 1
                j += 1

        # -------- Step 3: Remove trailing spaces --------
        # Join characters and strip extra spaces at the end
        return "".join(result).rstrip()