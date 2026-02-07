# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

# Example 1:
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = 0          # number of 'b's seen so far
        minDeletions = 0    # minimum deletions needed up to current position

        for char in s:
            if char == 'a':
                # Either delete this 'a' (minDeletions + 1)
                # Or delete all previous 'b's (bCount)
                minDeletions = min(minDeletions + 1, bCount)
            else:
                # Count 'b's that may need deletion later
                bCount += 1

        return minDeletions

