# https://leetcode.com/problems/longest-valid-parentheses/

# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Length of the input string.
        n = len(s)

        # Store the earliest position where each height occurs.
        # Offset by n so negative heights can also be used as indices.
        earliest = [-1] * (2 * n + 1)

        # Current balance/height of parentheses.
        height = 0

        # Length of the longest valid parentheses substring found.
        answer = 0

        # Height 0 occurs before processing the string.
        earliest[n] = 0

        # Process each character using 1-based position.
        for position, ch in enumerate(s, 1):

            if ch == "(":
                # Opening parenthesis increases the height.
                height += 1

                # Record the current position as the latest occurrence
                # of this height.
                earliest[height + n] = position

            else:
                # Mark the current height as invalid because we are
                # about to decrease it with a closing parenthesis.
                earliest[height + n] = -1

                # Closing parenthesis decreases the height.
                height -= 1

                # Convert the height into an array index.
                index = height + n

                # If this height has not been seen before after a valid
                # starting point, store the current position.
                if earliest[index] == -1:
                    earliest[index] = position
                else:
                    # Same height means the substring between the two
                    # positions has balanced parentheses.
                    answer = max(answer, position - earliest[index])

        # Return the length of the longest valid substring.
        return answer