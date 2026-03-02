# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

# Example 2:
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.

class Solution:
    def minSwaps(self, grid):
        # Get grid size (n x n matrix)
        n = len(grid)

        # This list will store count of trailing zeros for each row
        zeros = []

        # Step 1: Count trailing zeros in every row
        # We traverse from right → left until we hit a 1
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break   # stop when first 1 is found
            zeros.append(count)

        # Variable to store total swaps required
        swaps = 0

        # Step 2: Arrange rows to satisfy diagonal condition
        # For row i, we need at least (n - i - 1) trailing zeros
        for i in range(n):
            needed = n - i - 1
            j = i

            # Find a row below having enough trailing zeros
            while j < n and zeros[j] < needed:
                j += 1

            # If no such row exists → impossible configuration
            if j == n:
                return -1

            # Step 3: Bring that row up using adjacent swaps
            # (simulate bubble-up movement)
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                j -= 1
                swaps += 1

        # Total minimum swaps required
        return swaps