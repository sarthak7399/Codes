# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # Initialize an empty stack to keep track of indices of opening parentheses "("
        s = list(s)  # Convert the input string to a list of characters for easy manipulation
        for index, item in enumerate(s):  # Iterate through each character in the string along with its index
            if item == '(':  # If the character is an opening parenthesis
                stack.append(index)  # Push its index onto the stack
            elif item == ')':  # If the character is a closing parenthesis
                if stack:  # If the stack is not empty, meaning there is a corresponding opening parenthesis
                    stack.pop()  # Pop the topmost index from the stack to match the closing parenthesis
                else:  # If the stack is empty, meaning there is no matching opening parenthesis
                    s[index] = ''  # Mark the closing parenthesis for removal by replacing it with an empty string
        for item in stack:  # Iterate through any remaining indices in the stack
            s[item] = ''  # Mark unmatched opening parentheses for removal
        return "".join(s)  # Construct the final string by joining the characters that are not marked for removal
