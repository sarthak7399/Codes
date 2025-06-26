# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

# Example 1:
# Input: s = "1001010", k = 5
# Output: 5
# Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
# Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
# The length of this subsequence is 5, so 5 is returned.

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Step 1: Count all 0s (safe to include)
        zeros = s.count('0')

        # Step 2: Initialize
        value = 0
        count = 0
        power = 0

        # Step 3: Traverse from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                # Step 4: Try adding if within k
                if power < 32:
                    value += 1 << power
                    if value > k:
                        break
                    count += 1
                    power += 1
            else:
                # Step 5: Just increment power
                power += 1

        # Step 6: Total = allowed 1s + all 0s
        return count + zeros