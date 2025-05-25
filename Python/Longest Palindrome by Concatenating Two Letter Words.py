# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

# Example 1:
# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.

from collections import Counter

class Solution:
    def longestPalindrome(self, words):
        # Count the frequency of each word
        freq = Counter(words)
        
        ans = 0  # Length of the longest palindrome that can be formed
        has_center = False  # Flag to check if we can place a word in the center

        for word in list(freq.keys()):
            rev = word[::-1]  # Reverse of the current word
            
            # Case 1: Palindromic word (like "aa", "bb")
            if word == rev:
                # Use as many pairs as possible (2 words per pair, 4 letters)
                pairs = freq[word] // 2
                ans += pairs * 4
                freq[word] -= pairs * 2  # Update the count after using the pairs

                # If one word is left (like a single "aa"), it can be used in the center
                if freq[word] == 1:
                    has_center = True

            # Case 2: Non-palindromic word and its reverse exist (like "ab" and "ba")
            else:
                if rev in freq:
                    # Use the minimum number of pairs possible between the word and its reverse
                    pairs = min(freq[word], freq[rev])
                    ans += pairs * 4  # Each pair contributes 4 characters
                    freq[word] -= pairs
                    freq[rev] -= pairs  # Update counts after pairing

        # If there's a leftover palindromic word, it can be placed in the middle (2 characters)
        if has_center:
            ans += 2

        return ans
