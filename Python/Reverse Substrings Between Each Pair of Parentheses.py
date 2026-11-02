# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

# Example 2:
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Stack to store the starting index of each pair of parentheses.
        ind_stack: deque[int] = deque()

        # List to store characters of the result.
        res: list[str] = []

        # Traverse each character in the string.
        for char in s:
            if char == "(":
                # Store the current length as the start index
                # of the substring that needs to be reversed.
                ind_stack.append(len(res))

            elif char == ")":
                # Get the start index of the current parentheses pair.
                start_ind: int = ind_stack.pop()

                # Reverse the substring inside the parentheses.
                res[start_ind:] = res[start_ind:][::-1]

            else:
                # Add normal characters to the result.
                res.append(char)

        # Convert the character list into the final string.
        return "".join(res)