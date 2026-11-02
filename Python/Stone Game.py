# https://leetcode.com/problems/stone-game/

# Example 1:
# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # With an even number of piles, the first player can always
        # follow an optimal strategy and guarantee a win.
        return True