# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

# Example 1:
# Input: s = "3902"
# Output: true
# Explanation:
# Initially, s = "3902"
# First operation:
# (s[0] + s[1]) % 10 = (3 + 9) % 10 = 2
# (s[1] + s[2]) % 10 = (9 + 0) % 10 = 9
# (s[2] + s[3]) % 10 = (0 + 2) % 10 = 2
# s becomes "292"
# Second operation:
# (s[0] + s[1]) % 10 = (2 + 9) % 10 = 1
# (s[1] + s[2]) % 10 = (9 + 2) % 10 = 1
# s becomes "11"
# Since the digits in "11" are the same, the output is true.

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Keep reducing the string until only 2 characters remain
        while len(s) != 2:
            s1 = ""
            # Iterate through adjacent pairs of characters
            for i in range(1, len(s)):
                # Convert chars to numeric form (0–25), sum adjacent pairs,
                # take modulo 10 to limit result to a single digit
                x = ((ord(s[i]) - ord('a')) + (ord(s[i - 1]) - ord('a'))) % 10
                # Convert back to character ('a' + x)
                s1 += chr(x + ord('a'))
            # Update s with the new reduced string
            s = s1
        # Check if the final two characters are the same
        return s[0] == s[1]
