# https://leetcode.com/problems/find-common-characters/

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the dictionary to store minimum frequency of each character
        min_freq = {chr(i): float('inf') for i in range(ord('a'), ord('z') + 1)}

        # Calculate the frequency of each character in each word and update the minimum frequency
        for word in words:
            char_count = {}
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
            
            for char in min_freq:
                if char in char_count:
                    min_freq[char] = min(min_freq[char], char_count[char])
                else:
                    min_freq[char] = 0
        
        # Collect the common characters with the correct minimum frequency
        result = []
        for char, freq in min_freq.items():
            if freq > 0:
                result.extend([char] * freq)
        
        return result