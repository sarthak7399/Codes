# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

# Example 1:
# Input: s = "bcbbbcba"
# Output: 4
# Explanation:
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Store the maximum length of a valid substring found so far.
        res = 0

        # Left boundary of the sliding window.
        l = 0

        # Frequency map to keep track of character occurrences
        # inside the current window.
        fq = defaultdict(int)

        # Expand the window by moving the right pointer.
        for r, ch in enumerate(s):
            # Add the current character to the window.
            fq[ch] += 1

            # If the current character appears more than twice,
            # shrink the window from the left until the condition is restored.
            while fq[ch] > 2:
                fq[s[l]] -= 1
                l += 1

            # Update the maximum valid window length.
            res = max(res, r - l + 1)

        return res