# https://leetcode.com/problems/generate-parentheses/

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Base case for n = 1.
        if n == 1:
            return ["()"]

        # One opening parenthesis is already added initially,
        # so we need n - 1 more opening and closing parentheses.
        n -= 1

        # Store all valid combinations.
        res = []

        def dfs(O, C, s):
            # If no parentheses are left to place,
            # add the final closing parenthesis and store the result.
            if not O and not C:
                res.append(s + ")")
                return

            # We can add an opening parenthesis if some are remaining.
            if O > 0:
                dfs(O - 1, C, s + "(")

            # We can add a closing parenthesis only when the number
            # of remaining closing parentheses is at least the number
            # of remaining opening parentheses.
            if C >= O:
                dfs(O, C - 1, s + ")")

        # Start with one opening parenthesis.
        dfs(n, n, "(")

        # Return all valid parentheses combinations.
        return res