# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

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

        # Store the frequency of each lowercase English letter
        # Extra slots are added so the array can be divided
        # into four groups of eight characters.
        l = [0] * 32

        # Count the occurrence of every character from 'a' to 'z'
        for i in range(26):
            l[i] = word.count(chr(97 + i))

        # Place the most frequent characters first so that
        # they receive the minimum number of button pushes.
        l.sort(reverse=True)

        res = 0

        # Assign characters to groups of 8:
        # First 8 characters  -> 1 push each
        # Next 8 characters   -> 2 pushes each
        # Next 8 characters   -> 3 pushes each
        # Last 8 characters   -> 4 pushes each
        for i in range(4):
            for j in range(8):

                # Add frequency × number of pushes required
                res += (i + 1) * l[8 * i + j]

        return res