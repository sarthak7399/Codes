# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

# Example 1:
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

class Solution:
    def minInsertions(self, s: str) -> int:
        # Count unmatched opening parentheses and required insertions.
        open = ans = 0
        i = 0

        # Traverse the string.
        while i < len(s):
            if s[i] == '(':
                # Each opening parenthesis requires two closing parentheses.
                open += 1
            else:
                # Step 1: Ensure the closing parentheses form a "))" pair.
                if i + 1 < len(s) and s[i + 1] == ')':
                    # The next character is ')', so use it as the second one.
                    i += 1
                else:
                    # Insert a ')' to complete the required pair.
                    ans += 1

                # Step 2: Match the "))" pair with an opening parenthesis.
                if open > 0:
                    # Match with an existing unmatched '('.
                    open -= 1
                else:
                    # Insert an '(' because no unmatched opening exists.
                    ans += 1

            # Move to the next unprocessed character.
            i += 1

        # Each remaining '(' requires two closing parentheses.
        return ans + open * 2