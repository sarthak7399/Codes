# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

# Example 1:
# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32

class Solution:
    def minPartitions(self, n: str) -> int:
        # The minimum number of deci-binary numbers required
        # equals the maximum digit present in the string.
        #
        # A deci-binary number contains only digits 0 or 1.
        # To construct a digit 'd', we need at least 'd'
        # such numbers stacked together.
        #
        # Example:
        # n = "82734"
        # Maximum digit = 8
        # → At least 8 deci-binary numbers are needed.

        # max(n) gives the largest character digit,
        # convert it to integer before returning.
        return int(max(n))