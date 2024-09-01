# https://leetcode.com/problems/score-of-a-string/

# Example 1:
# Input: s = "hello"
# Output: 13
# Explanation:
# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        for i in range(len(s)-1):
            score+=abs(ord(s[i])-ord(s[i+1]))
        return score