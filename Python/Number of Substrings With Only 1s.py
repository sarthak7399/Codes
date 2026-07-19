# https://leetcode.com/problems/number-of-substrings-with-only-1s/

# Example 1:
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.

class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        left = 0       # start index of current block of consecutive '1's
        count = 0      # total number of valid substrings

        for right in range(len(s)):
            if s[right] == '0':
                left = right + 1   # reset block when '0' appears
            else:
                # number of new substrings ending at 'right'
                count = (count + (right - left + 1) % mod) % mod

        return count
