# https://leetcode.com/problems/find-missing-and-repeated-values/

# Example 1:
# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n: int = len(grid)  # Get the size of the grid (n x n)
        size: int = n * n  # Total numbers expected in the grid (1 to n^2)
        freq: List[int] = [0] * (size + 1)  # Frequency array to track occurrences
        repeated: int = -1  # Variable to store the repeated number
        missing: int = -1  # Variable to store the missing number

        # Count occurrences of each number in the grid
        for row in grid:
            for num in row:
                freq[num] += 1

        # Identify the repeated and missing numbers
        for num in range(1, size + 1):
            if freq[num] == 2:  # Number appears twice
                repeated = num
            if freq[num] == 0:  # Number is missing
                missing = num

        return [repeated, missing]  # Return the results
