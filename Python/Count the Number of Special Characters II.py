# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

# Example 1:
# Input: word = "aaAbcBC"
# Output: 3
# Explanation:
# The special characters are 'a', 'b', and 'c'.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        # Store last occurrence index of lowercase letters
        last_lower = {}

        # Store first occurrence index of uppercase letters
        first_upper = {}

        # Track letters that become invalid
        # (i.e., lowercase appears after uppercase)
        invalid = set()

        # Traverse string with indices
        for i, ch in enumerate(word):
            letter = ch.lower()

            if ch.islower():
                # Update last seen position of lowercase letter
                last_lower[letter] = i

                # If uppercase already appeared before this lowercase,
                # then this letter is invalid
                if letter in first_upper:
                    invalid.add(letter)

            else:
                # Store only the first occurrence of uppercase letter
                if letter not in first_upper:
                    first_upper[letter] = i

        special_count = 0  # Count valid special characters

        # A letter is special if:
        # 1. It appears as both lowercase and uppercase
        # 2. It is not marked invalid
        for letter in last_lower:
            if letter in first_upper and letter not in invalid:
                special_count += 1

        return special_count