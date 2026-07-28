# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

# Example 1:
# Input: s = "z"
# Output: "z"
# Explanation:
# A string of only one character is already the lexicographically smallest palindrome.

from string import ascii_lowercase
from typing import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Length of the string
        n = len(s)

        # Count the characters in the first half of the palindrome
        freq = Counter(s[:n >> 1])

        # Construct the lexicographically smallest first half
        # by placing characters in alphabetical order
        half = "".join(c * freq[c] for c in ascii_lowercase)

        # Middle character exists only for odd-length strings
        mid = s[n >> 1] if n & 1 else ""

        # Form the palindrome by appending the reverse of the first half
        return half + mid + half[::-1]