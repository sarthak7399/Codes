# https://leetcode.com/problems/longest-palindrome/

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = {}  # Use a dictionary to count characters
        max_length = 0  # Maximum length of a palindrome

        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1  # Efficiently get and update count

        # Count palindromes considering even and odd-length cases
        for count in char_counts.values():
            max_length += count // 2 * 2  # Count even-length palindromes
            if count % 2 == 1 and max_length % 2 == 0:  # Account for odd-length palindromes
                max_length += 1

        return max_length