# https://leetcode.com/problems/circular-sentence/

# Example 1:
# Input: sentence = "leetcode exercises sound delightful"
# Output: true
# Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
# - leetcode's last character is equal to exercises's first character.
# - exercises's last character is equal to sound's first character.
# - sound's last character is equal to delightful's first character.
# - delightful's last character is equal to leetcode's first character.
# The sentence is circular.

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Get the length of the sentence
        n = len(sentence)
        
        # First check: Compare first and last character of sentence
        # For a circular sentence, they must match
        if sentence[0] != sentence[n-1]:
            return False
            
        # Iterate through the sentence, starting from index 1 to n-2
        # We don't need to check first and last characters again
        for i in range(1, n-1):
            # When we find a space character
            if sentence[i] == ' ':
                # Check if the character before space (last char of current word)
                # matches the character after space (first char of next word)
                if sentence[i-1] != sentence[i+1]:
                    return False
                    
        # If we made it through all checks, the sentence is circular
        return True