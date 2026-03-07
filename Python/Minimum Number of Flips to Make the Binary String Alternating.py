# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

# Example 1:
# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".

class Solution:
    def minFlips(self, s: str) -> int:
        # Length of original string
        n = len(s)

        # Duplicate string to simulate all rotations
        # Any rotation of s will appear as a substring of s+s
        t = s + s

        # diff1 → number of mismatches with pattern "010101..."
        # diff2 → number of mismatches with pattern "101010..."
        diff1 = 0
        diff2 = 0

        # Store minimum flips needed
        ans = float('inf')

        # Traverse doubled string
        for i in range(2 * n):

            # Expected characters for both alternating patterns
            expect1 = '0' if i % 2 == 0 else '1'   # pattern: 010101...
            expect2 = '1' if i % 2 == 0 else '0'   # pattern: 101010...

            # Count mismatches for both patterns
            if t[i] != expect1:
                diff1 += 1
            if t[i] != expect2:
                diff2 += 1

            # Maintain sliding window of size n
            if i >= n:
                # Expected characters for the element leaving the window
                old_expect1 = '0' if (i - n) % 2 == 0 else '1'
                old_expect2 = '1' if (i - n) % 2 == 0 else '0'

                # Remove its contribution from mismatch count
                if t[i - n] != old_expect1:
                    diff1 -= 1
                if t[i - n] != old_expect2:
                    diff2 -= 1

            # When window size becomes n, evaluate answer
            if i >= n - 1:
                ans = min(ans, diff1, diff2)

        # Minimum flips required for any rotation
        return ans