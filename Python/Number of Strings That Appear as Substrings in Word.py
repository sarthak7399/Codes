# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

# Example 1:
# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3
# Explanation:
# - "a" appears as a substring in "abc".
# - "abc" appears as a substring in "abc".
# - "bc" appears as a substring in "abc".
# - "d" does not appear as a substring in "abc".
# 3 of the strings in patterns appear as a substring in word.

from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Stores the number of patterns that appear as
        # substrings in 'word'
        c = 0

        # Check each pattern one by one
        for p in patterns:

            # If the pattern exists inside 'word',
            # increment the count
            if p in word:
                c += 1

        # Return the total number of matching patterns
        return c