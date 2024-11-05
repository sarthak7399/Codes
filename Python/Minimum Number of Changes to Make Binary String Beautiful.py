# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

# Example 1:
# Input: s = "1001"
# Output: 2
# Explanation: We change s[1] to 1 and s[3] to 0 to get string "1100".
# It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
# It can be proven that 2 is the minimum number of changes needed to make the string beautiful.

class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1]:
                count += 1
            i += 2
        return count