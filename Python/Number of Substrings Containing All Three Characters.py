# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

# Example 1:
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}  # Track frequency of 'a', 'b', and 'c'
        
        for right in range(len(s)):
            char_count[s[right]] += 1  # Expand window by adding right character
            
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                count += len(s) - right  # Count all valid substrings ending at `right`
                char_count[s[left]] -= 1  # Shrink window from the left
                left += 1
        
        return count
