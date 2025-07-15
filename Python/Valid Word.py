# https://leetcode.com/problems/valid-word/

# Example 1:
# Input: word = "234Adas"
# Output: true
# Explanation:
# This word satisfies the conditions.

class Solution:
    def isValid(self, word: str) -> bool:
         # Rule 1: Word must have length at least 3
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")  # Set of vowel characters (both lowercase and uppercase)
        v = c = 0  # Counters for number of vowels and consonants

        for ch in word:
            if ch.isdigit():
                continue  # Digits are allowed but ignored in vowel/consonant count
            if ch.isalpha():  # Check if character is a letter
                # Increment vowel count if it's a vowel, else increment consonant count
                # := → this is the walrus operator (introduced in Python 3.8).
                # It assigns a value to a variable as part of an expression.
                (v := v + 1) if ch in vowels else (c := c + 1)
            else:
                return False  # Invalid character (not letter or digit)

        # Word is valid only if it contains at least one vowel and at least one consonant
        return v > 0 and c > 0