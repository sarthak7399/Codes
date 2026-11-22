# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

# Example 1:
# Input: s = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
# Hence, every 'a' appears before every 'b' and we return true.

class Solution:
    def checkString(self, s: str) -> bool:
        # Tracks whether character 'b' has been encountered
        seenB = False

        # Iterate through each character in the string
        for c in s:

            # Mark that 'b' has been encountered
            if c == 'b':
                seenB = True

            # If 'b' was already encountered and 'a' appears afterwards,
            # the string does not satisfy the required order
            elif seenB:
                return False

        # Return True if all 'a' characters appear before 'b' characters
        return True