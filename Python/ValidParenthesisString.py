# https://leetcode.com/problems/valid-parenthesis-string

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "(*)"
# Output: true

# Method 1 : Maintain two stacks for tracking the positions of '(' and '*', Time Complexity O(N), Space Complexity O(N)
class Solution:
    def checkValidString(self, s: str) -> bool:
        # Maintain two stacks for tracking the positions of '(' and '*'
        left_paren_stack = []
        star_stack = []       
        for i, char in enumerate(s):
            if char == '(':
                left_paren_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:  # char is ')'
                if left_paren_stack:
                    left_paren_stack.pop()  # Match '(' with ')'
                elif star_stack:
                    star_stack.pop()  # Use '*' as '('
                else:
                    return False  # No valid character to match ')'        
        # Match remaining '(' with '*' if possible
        while left_paren_stack and star_stack:
            if left_paren_stack[-1] < star_stack[-1]:
                left_paren_stack.pop()
                star_stack.pop()
            else:
                break        
        # If there are still unmatched '(' characters
        if left_paren_stack:
            return False        
        return True

# Method 2 : Maintain two variables for tracking the positions of '(' and '*', Time Complexity O(N), Space Complexity O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0,0
        for c in s:
            if c == "(":
                lo, hi = lo + 1, hi + 1
            elif c == ")":
                lo, hi = lo - 1, hi -1
            else:
                lo = lo - 1
                hi = hi + 1
            if hi < 0:
                return False
            if lo < 0:
                lo = 0
        return lo==0