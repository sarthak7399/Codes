# https://leetcode.com/problems/stone-game-viii/

# Example 1:
# Input: stones = [-1,2,-3,4,-5]
# Output: 5
# Explanation:
# - Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
#   value 2 on the left. stones = [2,-5].
# - Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
#   the left. stones = [-3].
# The difference between their scores is 2 - (-3) = 5.

from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Number of stones in the array.
        n = len(stones)

        # Convert stones into prefix sums.
        # After this, stones[i] represents the sum of
        # all original stones from index 0 to i.
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # Start from the largest possible prefix.
        # best represents the maximum score difference the
        # current player can achieve from the current state.
        best = stones[-1]

        # Process possible moves from right to left.
        # For each prefix ending at i, the current player can gain
        # stones[i], while the opponent can achieve 'best' afterwards.
        for i in range(n - 2, 0, -1):
            best = max(best, stones[i] - best)

        # Return the maximum score difference Alice can achieve.
        return best