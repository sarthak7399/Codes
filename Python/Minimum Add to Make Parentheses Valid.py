# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# Example 1:
# Input: s = "())"
# Output: 1

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Count unmatched opening and closing parentheses.
        open_c = close_c = 0

        # Traverse each character in the string.
        for c in s:
            if c == '(':
                # An opening parenthesis needs a matching closing one.
                open_c += 1

            elif c == ')' and open_c > 0:
                # Match the closing parenthesis with an unmatched opening one.
                open_c -= 1

            else:
                # No unmatched opening parenthesis exists,
                # so this closing parenthesis needs a matching opening one.
                close_c += 1

        # Add the unmatched opening and closing parentheses.
        return open_c + close_c