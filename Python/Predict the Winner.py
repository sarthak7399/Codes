# https://leetcode.com/problems/predict-the-winner/

# Example 1:
# Input: nums = [1,5,2]
# Output: false
# Explanation: Initially, player 1 can choose between 1 and 2. 
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
# Hence, player 1 will never be the winner and you need to return false.

from functools import cache
from typing import List

class Solution:
    def predictTheWinner(self, A: List[int]) -> bool:
        # Number of elements in the array
        n = len(A)

        # If the array length is even, Player 1 can always
        # choose a strategy that guarantees at least a tie.
        # ~n & 1 checks whether n is even.
        if ~n & 1:
            return True

        # maxDiff(i, j) returns the maximum score difference
        # (current player's score - opponent's score)
        # achievable using elements from index i to j.
        @cache
        def maxDiff(i: int, j: int) -> int:

            # Only one number is available, so the current
            # player must take it.
            if i == j:
                return A[i]

            # The current player can choose either:
            #
            # 1. Take A[i] from the left.
            #    The opponent then gets the remaining range.
            #
            # 2. Take A[j] from the right.
            #    The opponent then gets the remaining range.
            #
            # Subtracting the opponent's best score difference
            # gives the current player's net advantage.
            return max(
                A[i] - maxDiff(i + 1, j),
                A[j] - maxDiff(i, j - 1)
            )

        # Player 1 wins or ties if the final score difference
        # is greater than or equal to 0.
        return maxDiff(0, n - 1) >= 0