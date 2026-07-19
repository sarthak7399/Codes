# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4
# Output: false
# Explanation:
# In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).

class Solution:
    def areSimilar(self, mat, k):
        
        # Dimensions of the matrix
        m, n = len(mat), len(mat[0])
        
        # Reduce k to within bounds of row length
        # (shifting by n results in same row)
        k %= n
        
        # Traverse each row
        for i in range(m):
            for j in range(n):

                if i % 2 == 0:
                    # Even-indexed row → left shift by k
                    
                    # After left shift:
                    # element at index j should match element at (j + k) % n
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False

                else:
                    # Odd-indexed row → right shift by k
                    
                    # After right shift:
                    # element at index j should match element at (j - k) % n
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
        
        # If all elements match expected positions → matrices are similar
        return True