# https://leetcode.com/problems/stone-game-ix/

# Example 1:
# Input: stones = [2,1]
# Output: true
# Explanation: The game will be played as follows:
# - Turn 1: Alice can remove either stone.
# - Turn 2: Bob removes the remaining stone. 
# The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.

class Solution:
    def stoneGameIX(self, stones):
        # Count stones based on their remainder when divided by 3.
        a = 0  # Count of stones with remainder 0
        b = 0  # Count of stones with remainder 1
        c = 0  # Count of stones with remainder 2

        for x in stones:
            if x % 3 == 0:
                a += 1
            elif x % 3 == 1:
                b += 1
            else:
                c += 1

        # If the number of remainder-0 stones is even,
        # Alice needs at least one stone from both remainder groups.
        if a % 2 == 0:
            return b > 0 and c > 0

        # If the number of remainder-0 stones is odd,
        # Alice wins only when the counts of remainder-1 and
        # remainder-2 stones differ by more than 2.
        return abs(b - c) > 2