# https://leetcode.com/problems/find-the-original-typed-string-i/

# Example 1:
# Input: word = "abbcccc"
# Output: 5
# Explanation:
# The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1  # Start with 1 for the original string (flawless case)

        i, n = 0, len(word)

        while i < n:
            j = i
            # Move j forward while characters are the same — this identifies a block of repeating characters
            while j < n and word[j] == word[i]:
                j += 1

            # For a block of length L, we can create (L - 1) new strings
            # by changing one character in the block without making it flawless anymore
            ans += (j - i - 1)

            # Move to the next block of characters
            i = j

        return ans
