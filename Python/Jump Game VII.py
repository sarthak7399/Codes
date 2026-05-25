# https://leetcode.com/problems/jump-game-vii/

# Example 1:
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.

from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # BFS queue starting from index 0
        q = deque()
        q.append(0)

        # Tracks the farthest index already processed
        # to avoid revisiting ranges repeatedly
        far = 0

        # Perform BFS
        while len(q) > 0:
            i = q.popleft()

            # Reached last index
            if i == len(s) - 1:
                return True

            # Explore all reachable positions from current index
            #
            # Start from:
            # max(far, i + minJump)
            # because indices before 'far' are already processed
            #
            # End at:
            # i + maxJump
            for j in range(
                max(far, i + minJump),
                min(len(s), i + maxJump + 1)
            ):

                # Can only jump onto '0'
                if s[j] == '0':
                    q.append(j)

            # Update farthest processed boundary
            far = min(len(s), i + maxJump + 1)

        # Cannot reach last index
        return False