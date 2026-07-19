# https://leetcode.com/problems/alice-and-bob-playing-flower-game/

# Example 1:
# Input: n = 3, m = 2
# Output: 3
# Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # The answer is the number of (i, j) pairs with different parity (one odd, one even)
        # when i ∈ [1..n] and j ∈ [1..m].
        # Exactly half of the n*m pairs have opposite parity, so floor(n*m/2).
        return n * m // 2
