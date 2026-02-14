# https://leetcode.com/problems/champagne-tower/

# Example 1:
# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # Create a large enough 2D array (triangle tower)
        # 102 is used safely because max rows ≤ 100 in constraints
        tower = [[0] * 102 for _ in range(102)]
        
        # Pour all champagne into the top glass
        tower[0][0] = poured
        
        # Process row by row until the required query row
        for r in range(query_row + 1):
            for c in range(r + 1):
                
                # If glass overflows (>1 cup)
                if tower[r][c] > 1:
                    
                    # Extra champagne equally splits to next row
                    excess = (tower[r][c] - 1.0) / 2.0
                    
                    # Current glass can hold only 1 cup
                    tower[r][c] = 1
                    
                    # Left child glass receives half excess
                    tower[r+1][c] += excess
                    
                    # Right child glass receives half excess
                    tower[r+1][c+1] += excess
        
        # Return amount in requested glass
        return tower[query_row][query_glass]
