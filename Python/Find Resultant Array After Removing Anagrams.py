# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

# Example 1:
# Input: words = ["abba","baba","bbaa","cd","cd"]
# Output: ["abba","cd"]
# Explanation:
# One of the ways we can obtain the resultant array is by using the following operations:
# - Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
#   Now words = ["abba","baba","cd","cd"].
# - Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
#   Now words = ["abba","cd","cd"].
# - Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
#   Now words = ["abba","cd"].
# We can no longer perform any operations, so ["abba","cd"] is the final answer.

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # Initialize result list with the first word (since nothing precedes it)
        res = [words[0]]  
        n = len(words)

        # Helper function to check if two words are anagrams
        def compare(word1: str, word2: str) -> bool:
            # Frequency array for 26 lowercase letters
            freq = [0] * 26  

            # Increment frequency for each character in word1
            for ch in word1:
                freq[ord(ch) - ord("a")] += 1

            # Decrement frequency for each character in word2
            for ch in word2:
                freq[ord(ch) - ord("a")] -= 1

            # If all frequencies are 0 → they are anagrams
            return all(x == 0 for x in freq)

        # Traverse through the list starting from the 2nd word
        for i in range(1, n):
            # If current word is an anagram of previous word, skip it
            if compare(words[i], words[i - 1]):
                continue

            # Otherwise, add it to the result list
            res.append(words[i])

        # Return the final filtered list
        return res
