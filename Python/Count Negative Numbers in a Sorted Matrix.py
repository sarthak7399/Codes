# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0  # Total count of negative numbers

        # Traverse each row
        for i in range(len(grid)):
            # Traverse each column in the row
            for j in range(len(grid[i])):
                # Check if the current element is negative
                if grid[i][j] < 0:
                    count += 1

        return count
