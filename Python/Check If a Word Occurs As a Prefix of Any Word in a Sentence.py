# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

# Example 1:
# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Length of the searchWord to simplify substring checks
        l = len(searchWord)
        
        # Initialize a counter to keep track of the word position in the sentence
        count = 0
        
        # Split the sentence into words and iterate through them
        for word in sentence.split():
            count += 1  # Increment word position
            
            # Skip the word if its length is less than the searchWord
            if len(word) < len(searchWord):
                continue
            
            # Check if the searchWord is a prefix of the current word
            if searchWord == word[:l]:
                return count  # Return the position of the word
        
        # If no word matches the prefix, return -1
        return -1