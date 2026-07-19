# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

from typing import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Count the remaining occurrences of each character
        freq = Counter(s)

        # Keep track of characters already present in the stack
        seen = set()

        # Monotonic stack used to build the smallest subsequence
        stack = []

        for c in s:
            # One occurrence of the current character is now being processed
            freq[c] -= 1

            # Skip duplicate characters already included in the subsequence
            if c in seen:
                continue

            # Remove larger characters from the stack if:
            # 1. The current character is smaller
            # 2. The larger character will appear again later
            while stack and stack[-1] > c and freq[stack[-1]]:
                seen.remove(stack.pop())

            # Add the current character to the stack
            stack.append(c)
            seen.add(c)

        # Convert the stack into the final subsequence
        return "".join(stack)