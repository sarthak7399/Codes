# https://leetcode.com/problems/count-the-number-of-special-characters-i/

# Example 1:
# Input: word = "aaAbcBC"
# Output: 3
# Explanation:
# The special characters in word are 'a', 'b', and 'c'.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        # Store all characters in a set for O(1) lookup
        st = set(word)

        count = 0  # Count of special characters

        # Check all 26 English letters
        for i in range(26):

            # Generate lowercase character
            lower = chr(ord('a') + i)

            # Generate uppercase character
            upper = chr(ord('A') + i)

            # A character is special if both lowercase
            # and uppercase versions exist in the string
            if lower in st and upper in st:
                count += 1

        return count