# https://leetcode.com/problems/equal-sum-grid-partition-ii/

# Example 1:
# Input: grid = [[1,4],[2,3]]
# Output: true
# Explanation:
# A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.

import collections
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        # Dimensions
        n = len(grid)
        m = len(grid[0])
        
        # Prefix sums for rows and columns
        pref_row = [0] * n   # cumulative row sums
        pref_col = [0] * m   # cumulative column sums
        
        # Map: value → list of positions where it occurs
        mp = collections.defaultdict(list)
        
        # -------- Step 1: Build row prefix sums and map --------
        for i in range(n):
            row_sum = 0
            for j in range(m):
                val = grid[i][j]
                row_sum += val
                
                # Store position of each value
                mp[val].append((i, j))
            
            # Build prefix sum of rows
            pref_row[i] = row_sum + (pref_row[i - 1] if i > 0 else 0)
        
        # -------- Step 2: Build column prefix sums --------
        for j in range(m):
            col_sum = 0
            for i in range(n):
                col_sum += grid[i][j]
            
            # Build prefix sum of columns
            pref_col[j] = col_sum + (pref_col[j - 1] if j > 0 else 0)
        
        # Total sum of grid
        total = pref_row[-1]
        
        # -------- Helper: Check if we can remove a cell --------
        def can_remove(r1, c1, r2, c2, i, j):
            """
            Checks whether cell (i, j) can be removed from submatrix
            defined by top-left (r1, c1) and bottom-right (r2, c2)
            """
            rows = r2 - r1 + 1
            cols = c2 - c1 + 1
            
            # If only one cell → cannot remove (would leave empty)
            if rows * cols == 1:
                return False
            
            # If single row → can only remove from ends
            if rows == 1:
                return j == c1 or j == c2
            
            # If single column → can only remove from ends
            if cols == 1:
                return i == r1 or i == r2
            
            # Otherwise removal is always possible
            return True

        # -------- Step 3: Try horizontal cuts --------
        for i in range(n - 1):
            
            # Sum of top and bottom parts
            top = pref_row[i]
            bottom = total - top
            
            # If equal → valid partition
            if top == bottom:
                return True
            
            # Difference to fix by removing one element
            diff = abs(top - bottom)
            
            # If such value exists in grid
            if diff in mp:
                
                # If top is larger → remove from top part
                if top > bottom:
                    for x, y in mp[diff]:
                        if x <= i and can_remove(0, 0, i, m - 1, x, y):
                            return True
                else:
                    # Remove from bottom part
                    for x, y in mp[diff]:
                        if x > i and can_remove(i + 1, 0, n - 1, m - 1, x, y):
                            return True

        # -------- Step 4: Try vertical cuts --------
        for j in range(m - 1):
            
            # Sum of left and right parts
            left = pref_col[j]
            right = total - left
            
            # If equal → valid partition
            if left == right:
                return True
            
            # Difference to fix
            diff = abs(left - right)
            
            # If such value exists
            if diff in mp:
                
                # If left is larger → remove from left
                if left > right:
                    for x, y in mp[diff]:
                        if y <= j and can_remove(0, 0, n - 1, j, x, y):
                            return True
                else:
                    # Remove from right
                    for x, y in mp[diff]:
                        if y > j and can_remove(0, j + 1, n - 1, m - 1, x, y):
                            return True
        
        # No valid partition found
        return False