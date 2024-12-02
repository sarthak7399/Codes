# https://leetcode.com/problems/rotate-string/

# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Step 1: Check if lengths are different
        if len(s) != len(goal):
            return False
        
        # Step 2: Check if goal is a substring of s + s
        doubled_s = s + s
        return goal in doubled_s