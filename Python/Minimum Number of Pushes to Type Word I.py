# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

# Example 1:
# Input: word = "abcde"
# Output: 5
# Explanation: The remapped keypad given in the image provides the minimum cost.
# "a" -> one push on key 2
# "b" -> one push on key 3
# "c" -> one push on key 4
# "d" -> one push on key 5
# "e" -> one push on key 6
# Total cost is 1 + 1 + 1 + 1 + 1 = 5.
# It can be shown that no other mapping can provide a lower cost.

class Solution:
    def minimumPushes(self, word: str) -> int:

        # Stores the total number of button pushes required
        pushes = 0

        # Each key can contain up to 8 characters.
        # Characters at indices 0-7 require 1 push,
        # indices 8-15 require 2 pushes, and so on.
        for i in range(len(word)):
            pushes += (i // 8) + 1

        return pushes