# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:
# Input: s = "(1)+((2))+(((3)))"
# Output: 3

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            max_depth = max(max_depth, depth)
        return max_depth
