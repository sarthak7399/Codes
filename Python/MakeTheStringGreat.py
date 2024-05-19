# https://leetcode.com/problems/make-the-string-great/

# Example 1:
# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # Initialize an empty stack to keep track of characters
        for char in s:  # Iterate through each character in the string
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:  # Check if the current character forms a pair with the top character in the stack
                stack.pop()  # If yes, remove the top character from the stack
            else:
                stack.append(char)  # If not, add the current character to the stack
        return ''.join(stack)  # Convert the stack to a string and return it
