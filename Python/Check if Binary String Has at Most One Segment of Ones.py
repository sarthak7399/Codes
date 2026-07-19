# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

# Example 1:
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Traverse the string from the second character
        for i in range(1, len(s)):

            # If we see '1' after a '0', it means a new segment of 1s has started
            # Example: 110011 → second group of '1's appears
            # That means there are multiple segments of 1s → return False
            if s[i] == '1' and s[i - 1] == '0': 
                return False

        # If we never found a second '1' segment, then there is
        # at most one continuous segment of '1's
        return True