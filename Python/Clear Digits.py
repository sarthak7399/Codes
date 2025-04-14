# https://leetcode.com/problems/clear-digits/

# Example 1:
# Input: s = "abc"
# Output: "abc"
# Explanation:
# There is no digit in the string.

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []  # Stack to store non-digit characters

        for c in s:
            if c.isdigit():  # If the character is a digit
                if stack:  # Remove the last added character if stack is not empty
                    stack.pop()
            else:  # If it's not a digit, add it to the stack
                stack.append(c)

        return "".join(stack)  # Convert the stack back to a string
