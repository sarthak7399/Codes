# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

# Example 1:
# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Array to mark broken keys: 1 if broken, 0 if working
        brokenKeyMap = [0] * 26
        asciiA = ord('a')

        # Mark broken keys in the map
        for c in brokenLetters:
            brokenKeyMap[ord(c) - asciiA] = 1

        # Total number of words (starts at 1 since words = spaces + 1)
        word_count = 1
        # Words that cannot be typed because they contain broken letters
        broken_word_count = 0
        # Flag to check if the current word contains a broken key
        word_has_broken_key = False

        # Iterate through the text
        for c in text:
            if c == " ":
                # End of a word: check if it had a broken key
                if word_has_broken_key:
                    broken_word_count += 1
                # Reset for next word
                word_has_broken_key = False
                # Increase total word count
                word_count += 1
            else:
                # If character is broken and current word not yet marked as broken
                if not word_has_broken_key and brokenKeyMap[ord(c) - asciiA] > 0:
                    word_has_broken_key = True

        # Handle last word (loop ends without hitting a space)
        if word_has_broken_key:
            broken_word_count += 1

        # Valid words = total words - broken words
        return word_count - broken_word_count
