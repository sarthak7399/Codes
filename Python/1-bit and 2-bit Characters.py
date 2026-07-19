# https://leetcode.com/problems/1-bit-and-2-bit-characters/

# Example 1:
# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0

        # Move through the array:
        # 0 → single-bit char, move 1 step
        # 1 → two-bit char, move 2 steps
        while i < n - 1:
            i += bits[i] + 1

        # True only if last character is a single-bit '0'
        return i == n - 1
