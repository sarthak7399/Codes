# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

# Example 1:
# Input: n = 5, k = 2
# Output: 3
# Explanation: Here are the steps of the game:
# 1) Start at friend 1.
# 2) Count 2 friends clockwise, which are friends 1 and 2.
# 3) Friend 2 leaves the circle. Next start is friend 3.
# 4) Count 2 friends clockwise, which are friends 3 and 4.
# 5) Friend 4 leaves the circle. Next start is friend 5.
# 6) Count 2 friends clockwise, which are friends 5 and 1.
# 7) Friend 1 leaves the circle. Next start is friend 3.
# 8) Count 2 friends clockwise, which are friends 3 and 5.
# 9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        current_position = 0

        # Till 1 friend is left
        while n > 1:
            # Current position after k move, (k-1) to include current friend.
            current_position = (current_position + (k-1)) % n
            # Remove picked friend
            friends.pop(current_position)
            # Decrement total friends
            n -= 1

        # Return last friend
        return friends[0]