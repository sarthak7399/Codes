# https://leetcode.com/problems/count-commas-in-range/

# Example 1:
# Input: n = 1002
# Output: 3
# Explanation:
# The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

class Solution:
    def countCommas(self, n):
        # Numbers from 1 to 999 do not contain any commas.
        # Starting from 1,000, each number in this range
        # contributes one comma.
        #
        # Therefore, the total count is n - 999.
        # max(0, ...) ensures the result is not negative.
        return max(0, n - 999)