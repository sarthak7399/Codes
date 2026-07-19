# https://leetcode.com/problems/sort-vowels-in-a-string/

# Example 1:
# Input: s = "lEetcOde"
# Output: "lEOtcede"
# Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.

from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        # Count frequency of each character in the string
        freq = Counter(s)

        # String containing all vowels in sorted order (ASCII order)
        vowel = 'AEIOUaeiou'

        # 'count' = how many vowels have been placed so far
        # 'v' = frequency of current vowel we are filling
        # 'j' = index pointer into `vowel`
        count, v, j = 0, freq['A'], 0

        # Convert input string into list for mutability
        s = list(s)

        for i, c in enumerate(s):
            # Check if c is a vowel using a bitmask trick
            # (0x208222 >> (ord(c) & 31)) & 1 == 1 if c is vowel
            if ((0x208222 >> (ord(c) & 31)) & 1) == 0:
                continue  # skip if not vowel

            # If we have already placed all instances of current vowel,
            # move to next vowel in sorted order
            while count >= v:
                j += 1
                v += freq[vowel[j]]

            # Replace current vowel with the correct sorted vowel
            s[i] = vowel[j]

            # Increment count of vowels placed
            count += 1

        # Join list back to string
        return "".join(s)
