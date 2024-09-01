# https://leetcode.com/problems/word-break-ii/

# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]

# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []  # List to store the final sentences
        current_sequence = []  # List to store the current sequence of words
        word_set = set(wordDict)  # Set for fast lookup of words in the dictionary

        def dfs(start_index):
            if start_index == len(s):
                # If we reach the end of the string, join the current sequence into a sentence
                result.append("".join(current_sequence[:-1]))  # Exclude the trailing space
                return
            for end_index in range(start_index + 1, len(s) + 1):
                if s[start_index: end_index] in word_set:
                    current_sequence.append(s[start_index:end_index])  # Add the word to the sequence
                    current_sequence.append(" ")  # Add a space after the word
                    dfs(end_index)  # Recurse for the next part of the string
                    current_sequence.pop()  # Remove the space
                    current_sequence.pop()  # Remove the word

        dfs(0)  # Start the DFS from the beginning of the string
        return result
