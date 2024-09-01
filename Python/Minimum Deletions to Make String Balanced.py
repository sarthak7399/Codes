# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

# Example 1:
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = 0
        minDeletions = 0
        for char in s:
            if char == 'a':
                minDeletions = min(minDeletions + 1, bCount)
            else:
                bCount += 1   
        return minDeletions
