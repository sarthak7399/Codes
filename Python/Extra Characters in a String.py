# https://leetcode.com/problems/extra-characters-in-a-string/

# Example 1:
# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

class Solution:
    def __init__(self):
        self.dp = [-1] * 51  # Initialize dp array with -1 values
        
    def minExtraChar(self, s, dictionary):
        return self.minExtraCharHelper(s, dictionary, 0)
    
    def minExtraCharHelper(self, s, dictionary, i):
        if i == len(s):
            return 0

        if self.dp[i] == -1:
            self.dp[i] = 1 + self.minExtraCharHelper(s, dictionary, i + 1)  # Initialize with one extra character.

            for w in dictionary:
                if s[i:i+len(w)] == w:
                    self.dp[i] = min(self.dp[i], self.minExtraCharHelper(s, dictionary, i + len(w)))  # Update if a word in the dictionary is found.

        return self.dp[i]  # Return the minimum extra characters starting from position i