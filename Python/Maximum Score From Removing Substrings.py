# https://leetcode.com/problems/maximum-score-from-removing-substrings/

# Example 1:
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0  # Initialize total score result

        # Decide which substring removal gives higher score
        # Always remove higher scoring substring first
        if y > x:
            top = "ba"
            top_score = y
            bot = "ab"
            bot_score = x
        else:
            top = "ab"
            top_score = x
            bot = "ba"
            bot_score = y

        # Step 1: Remove all top substrings greedily using a stack
        stack: list[str] = []
        for char in s:
            # If top substring is formed at stack top, remove it and add score
            if char == top[1] and stack and stack[-1] == top[0]:
                res += top_score
                stack.pop()  # Remove first character of the top substring
            else:
                stack.append(char)  # Otherwise keep character

        # Step 2: Remove remaining bot substrings from the stack
        new_stack: list[str] = []
        for char in stack:
            # If bot substring is formed, remove it and add score
            if char == bot[1] and new_stack and new_stack[-1] == bot[0]:
                res += bot_score
                new_stack.pop()  # Remove first character of the bot substring
            else:
                new_stack.append(char)

        return res  # Return total score after removing substrings
