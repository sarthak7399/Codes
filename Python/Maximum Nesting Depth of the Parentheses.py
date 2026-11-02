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
        # Track the current nesting depth.
        depth = 0

        # Store the maximum depth seen so far.
        max_depth = 0

        # Traverse each character in the string.
        for char in s:
            if char == '(':
                # Opening parenthesis increases the depth.
                depth += 1

            elif char == ')':
                # Closing parenthesis decreases the depth.
                depth -= 1

            # Update the maximum depth reached so far.
            max_depth = max(max_depth, depth)

        # Return the maximum nesting depth.
        return max_depth