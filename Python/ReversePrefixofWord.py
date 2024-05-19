# https://leetcode.com/problems/reverse-prefix-of-word/

# Example 1:
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the character 'ch' in the word
        char_index = word.find(ch)
        # If the character 'ch' is found in the word
        if char_index != -1:
            # Reverse the substring from the start of the word to the index of 'ch'
            reversed_prefix = word[:char_index+1][::-1]
            # Concatenate the reversed prefix with the remaining part of the word
            return reversed_prefix + word[char_index+1:]
        # If the character 'ch' is not found in the word, return the original word
        return word