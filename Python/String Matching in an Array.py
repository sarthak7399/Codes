# https://leetcode.com/problems/string-matching-in-an-array/

# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Initialize an empty list to store the result
        result = []
        
        # Get the number of words in the input list
        n = len(words)
        
        # Loop through each word in the list (outer loop)
        for i in range(n):
            # Loop through each word again to compare (inner loop)
            for j in range(n):
                # Ensure that we're not comparing the same word with itself
                if i != j and words[i] in words[j]:
                    # If word[i] is found as a substring within word[j], add word[i] to the result list
                    result.append(words[i])
                    # Once found, break the inner loop to avoid adding the same word multiple times
                    break
        
        # Return the list of words that are substrings of other words
        return result
