# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

# Example 1:
# Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
# Output: 100
# Explanation:
# In this example:
# The 1st child (green) moves on the path (0,0) -> (1,1) -> (2,2) -> (3, 3).
# The 2nd child (red) moves on the path (0,3) -> (1,2) -> (2,3) -> (3, 3).
# The 3rd child (blue) moves on the path (3,0) -> (3,1) -> (3,2) -> (3, 3).
# In total they collect 1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100 fruits.

from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # Step 1: Total fruits collected by going diagonally from top-left to bottom-right
        total = sum(fruits[i][i] for i in range(n))

        # Step 2: Initialize DP arrays for right edge and bottom edge
        right_path = [0] * 3  # Tracks max fruits from top row to right edge
        right_path[0] = fruits[0][n - 1]  # First step: (0, n-1)

        bottom_path = [0] * 3  # Tracks max fruits from bottom row to bottom edge
        bottom_path[0] = fruits[n - 1][0]  # First step: (n-1, 0)

        window = 2  # Width of the sliding window used for DP (will expand and shrink)

        # Step 3: Dynamic Programming for all steps (from 1 to n - 2)
        for step in range(1, n - 1):
            new_right = [0] * (window + 2)    # Temporary array for next right_path values
            new_bottom = [0] * (window + 2)   # Temporary array for next bottom_path values

            # For each distance from the corner (i.e., how far diagonally we are from the main diagonal)
            for dist in range(window):
                # Update right_path (moving along top row toward top-right corner)
                left = right_path[dist - 1] if dist - 1 >= 0 else 0
                mid = right_path[dist]
                right = right_path[dist + 1] if dist + 1 < len(right_path) else 0
                new_right[dist] = max(left, mid, right) + fruits[step][n - 1 - dist]

                # Update bottom_path (moving along bottom row toward bottom-left corner)
                left = bottom_path[dist - 1] if dist - 1 >= 0 else 0
                mid = bottom_path[dist]
                right = bottom_path[dist + 1] if dist + 1 < len(bottom_path) else 0
                new_bottom[dist] = max(left, mid, right) + fruits[n - 1 - dist][step]

            # Move to next step
            right_path = new_right
            bottom_path = new_bottom

            # Step 4: Adjust the window size depending on current step
            # This controls how far from the diagonal the path can go
            if window - n + 4 + step <= 1:
                window += 1
            elif window - n + 3 + step > 1:
                window -= 1

        # Step 5: Final answer = diagonal path + best right-edge path + best bottom-edge path
        return total + right_path[0] + bottom_path[0]
