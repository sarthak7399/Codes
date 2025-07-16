# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

# Example 1:
# Input: word = "dbca", numFriends = 2
# Output: "dbc"
# Explanation: 
# All possible splits are:
# "d" and "bca".
# "db" and "ca".
# "dbc" and "a".

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # If there's only one friend, return the full word as-is
        if numFriends == 1:
            return word

        # Length of the substrings to compare = total letters divided among friends
        leng = len(word) - numFriends + 1

        res = ''       # To store the maximum substring found
        l, r = 0, leng - 1  # Initial sliding window pointers

        # Slide the window across the string
        while l < len(word):
            # Compare current substring with the best one found so far
            if word[l:r + 1] > res:
                res = word[l:r + 1]
            l += 1
            r += 1

        return res  # Return the lexicographically largest substring of length `leng`
