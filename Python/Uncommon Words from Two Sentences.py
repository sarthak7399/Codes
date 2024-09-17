# https://leetcode.com/problems/uncommon-words-from-two-sentences/

# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Explanation:
# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

from typing import Counter, List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words
        words_s1 = s1.split()
        words_s2 = s2.split()
        # Combine all words into one list
        all_words = words_s1 + words_s2
        # Count the frequency of each word
        word_count = Counter(all_words)
        # Find words that occur exactly once
        return [word for word in word_count if word_count[word] == 1]