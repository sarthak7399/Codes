# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

# Example 1:
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

# For my reference, explaination of code from YT : https://www.youtube.com/watch?v=BI4h1IwfADs

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Vowels with their respective bitmask values
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        # Dictionary to store the first occurrence of each bitmask
        # We start with bitmask 0 at index -1, to handle the case when the entire string is valid
        first_occurrence = {0: -1}
        
        # Current bitmask and result variable
        mask = 0
        max_len = 0
        
        # Traverse the string
        for i, c in enumerate(s):
            # If the character is a vowel, update the bitmask
            if c in vowels:
                mask ^= vowels[c]
            
            # If the bitmask has been seen before, calculate the length of the substring
            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                # If this is the first time we've seen this bitmask, store the index
                first_occurrence[mask] = i
        
        return max_len