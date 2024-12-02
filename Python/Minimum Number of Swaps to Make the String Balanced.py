# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

# Example 1:
# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3.
# The resulting string is "[[]]".

class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        # Check if the string is balanced
        for c in s:
            # If the character is a closing bracket
            if c == '[':
                ans += 1    # Increase the number of opening brackets
            elif ans > 0:   # If the character is an opening bracket
                ans -= 1    # Decrease the number of opening brackets
        return (ans + 1) // 2   # Divide the number of opening brackets by 2