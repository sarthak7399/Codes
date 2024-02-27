# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]

from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column_starts_with = grid[0]        # Store the first row of the grid
        columns = [[] for _ in column_starts_with]            # Initialize a list to store the columns of the grid

        for row in grid:
            for j, element in enumerate(row):       # Iterate through each element in the row and append it to the corresponding column
                columns[j].append(element)
        equal_pairs = 0         # Initialize a variable to count the equal pairs

        for row in grid:
            for j, element in enumerate(column_starts_with):    # Iterate through each element in the first row
                if row[0] == element:       # Check if the first element of the row is equal to the element in the corresponding column
                    if row == columns[j]:       # Check if the entire row is equal to the column
                        equal_pairs += 1
                        
        return equal_pairs