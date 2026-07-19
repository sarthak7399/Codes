# https://leetcode.com/problems/jump-game-v/

# Example 1:
# Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# Output: 4
# Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
# Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
# Similarly You cannot jump from index 3 to index 2 or index 1.

from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # steps[i] = maximum jumps possible starting from index i
        # Initialize with 1 because each index itself counts as one position
        steps = [1 for i in range(len(arr))]

        # Monotonic decreasing stack (stores indices)
        stack = []

        n = len(arr)

        # Iterate through array + one extra iteration for cleanup
        for i in range(n + 1):

            # Process while current value is greater than stack top
            while len(stack) > 0 and (i == n or arr[stack[-1]] < arr[i]):

                # Pop indices with smaller value
                pop_indices = [stack.pop()]

                # Group equal values together
                while stack and arr[stack[-1]] == arr[pop_indices[0]]:
                    pop_indices.append(stack.pop())

                # Process all popped indices
                for j in pop_indices:

                    # Jump from j → i (right side)
                    if i < n and i - j <= d:
                        steps[i] = max(steps[i], steps[j] + 1)

                    # Jump from j → stack[-1] (left side)
                    if len(stack) > 0 and j - stack[-1] <= d:
                        steps[stack[-1]] = max(
                            steps[stack[-1]],
                            steps[j] + 1
                        )

            # Add current index to stack
            if i < n:
                stack.append(i)

        # Maximum jumps among all starting positions
        return max(steps)