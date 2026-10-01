# https://leetcode.com/problems/valid-parentheses/

# Example 2:
# Input: s = "()[]{}"
# Output: true

class Solution:

    def isValid(self, s: str) -> bool:

        # Stack to store opening brackets.
        st = []

        # Traverse each character in the string.
        for c in s:

            # If it is an opening bracket, push it onto the stack.
            if c in '({[':
                st.append(c)

            else:
                # If there is no opening bracket to match,
                # the string is invalid.
                if not st:
                    return False

                # Get the most recent opening bracket.
                top = st.pop()

                # Check if the closing bracket matches the opening bracket.
                if (c == ')' and top != '(') or \
                   (c == '}' and top != '{') or \
                   (c == ']' and top != '['):

                    # Mismatched brackets make the string invalid.
                    return False

        # The string is valid only if no unmatched opening
        # brackets are left in the stack.
        return not st