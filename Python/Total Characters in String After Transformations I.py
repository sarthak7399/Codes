# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

# Example 1:
# Input: s = "abcyy", t = 2
# Output: 7
# Explanation:
# First Transformation (t = 1):
# 'a' becomes 'b'
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'y' becomes 'z'
# 'y' becomes 'z'
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'd' becomes 'e'
# 'z' becomes "ab"
# 'z' becomes "ab"
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7  # Modulo to prevent overflow in large computations
        cnt = [0] * 26   # Array to keep count of each character from 'a' to 'z'
        res = len(s)     # Initial length of the string
        z = 25           # Start from character 'z' (index 25)

        # Count frequency of each character in the initial string
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        # Perform t transformations
        for _ in range(t):
            # Every time we process 'z', it will turn into 'a' (since 'z' + 1 = 'a' circularly)
            res = (res + cnt[z]) % MOD  # Increase result length by the count of 'z' (transformation creates new characters)
            
            # Add all 'z's (now turning to 'a') to the count of 'a' (index 0, i.e., (25+1)%26)
            cnt[(z + 1) % 26] = (cnt[(z + 1) % 26] + cnt[z]) % MOD

            # Move z one character back (circularly from 'z' → 'y' → ... → 'a')
            z = (z + 25) % 26  # Equivalent to (z - 1) % 26, but avoids negative index

        return res  # Return final length after all transformations
