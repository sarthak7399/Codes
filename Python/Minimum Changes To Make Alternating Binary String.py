# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

# Example 1:
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.

class Solution:
    def minOperations(self, s: str) -> int:
        # c → counts mismatches with pattern starting with '1'
        # j → expected bit for the alternating pattern (0 → 1 → 0 → 1 ...)
        # n → length of the string
        c, j, n = 0, 0, len(s)

        # Traverse each character in the string
        for ch in s:
            # If the current character matches the expected bit (j),
            # then it is a mismatch for the opposite alternating pattern.
            if int(ch) == j:
                c += 1

            # Flip expected bit (0 -> 1 or 1 -> 0)
            j ^= 1

        # Two possible alternating patterns exist:
        # Pattern 1: 010101...
        # Pattern 2: 101010...
        #
        # c represents the number of operations needed to convert
        # the string to one pattern, while (n - c) represents the
        # operations for the other pattern.
        #
        # Return the minimum of the two.
        return min(c, n - c)