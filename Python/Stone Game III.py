# https://leetcode.com/problems/stone-game-iii/

# Input: stoneValue = [1,2,3,-9]
# Output: "Alice"
# Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
# If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
# If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
# Remember that both play optimally so here Alice will choose the scenario that makes her win.

from functools import cache
from typing import List

class Solution:
    # Maps the final score difference to the game result:
    # Negative -> Bob, Zero -> Tie, Positive -> Alice
    s = ["Bob", "Tie", "Alice"]

    def stoneGameIII(self, A: List[int]) -> str:
        # Total number of stones
        n = len(A)

        # maxDiff(i) returns the maximum score difference
        # (current player's score - opponent's score)
        # starting from index i.
        @cache
        def maxDiff(i: int) -> int:

            # No stones are left, so the score difference is 0.
            if i == n:
                return 0

            # Initialize all choices with a very small value.
            a = b = c = -5e7

            # Option 1: Take one stone.
            # Subtract the opponent's best score difference
            # from the current player's gained score.
            if i < n:
                a = A[i] - maxDiff(i + 1)

            # Option 2: Take two stones.
            if i + 1 < n:
                b = A[i] + A[i + 1] - maxDiff(i + 2)

            # Option 3: Take three stones.
            if i + 2 < n:
                c = A[i] + A[i + 1] + A[i + 2] - maxDiff(i + 3)

            # Choose the move that gives the maximum advantage.
            return max(a, b, c)

        # Calculate Alice's maximum possible score difference.
        d = maxDiff(0)

        # Convert the score difference into:
        # d < 0 -> "Bob"
        # d = 0 -> "Tie"
        # d > 0 -> "Alice"
        return self.s[(d > 0) - (d < 0) + 1]