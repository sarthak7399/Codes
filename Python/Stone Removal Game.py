# https://leetcode.com/problems/stone-removal-game/

# Example 1:
# Input: n = 12
# Output: true
# Explanation:
# Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
# Bob cannot remove 9 stones, so Alice wins.

class Solution:
    def canAliceWin(self, n: int) -> bool:
        # t tracks whose turn it is (0 = Alice, 1 = Bob)
        # pile represents the number of stones to be removed
        t, pile = 0, 10

        # Continue while enough stones are available
        while n >= pile:

            # Remove the current pile of stones
            n -= pile

            # Decrease the pile size by 1 for the next turn
            pile -= 1

            # Toggle the turn between Alice and Bob
            t ^= 1

        # Return True if it is Alice's turn to lose (Bob wins)
        # based on the final turn parity
        return bool(t & 1)