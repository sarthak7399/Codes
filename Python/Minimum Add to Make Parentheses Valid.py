# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# Example 1:
# Input: s = "())"
# Output: 1

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_c = close_c = 0
        for c in s:
            if c == '(':    # Opening Parenthesis
                open_c += 1
            elif c == ')' and open_c > 0:   # Closing Parenthesis and open Parenthesis exists
                open_c -= 1
            else:       # Closing Parenthesis and no open Parenthesis
                close_c += 1    
        return open_c + close_c     # Add the number of opening and closing Parenthesis