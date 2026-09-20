# https://leetcode.com/problems/reverse-degree-of-a-string/

# Example 1:
# Input: s = "abc"
# Output: 148
# Explanation:
# Letter	Index in Reversed Alphabet	Index in String	Product
# 'a'	26	1	26
# 'b'	25	2	50
# 'c'	24	3	72
# The reversed degree is 26 + 50 + 72 = 148.

class Solution:
    def reverseDegree(self, s: str) -> int:
        # Store the sum of all reverse-degree contributions.
        total = 0

        # Process each character along with its 0-based index.
        for i, c in enumerate(s):
            # Calculate the reverse alphabetical value.
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1.
            reverse_value = 26 - (ord(c) - ord('a'))

            # Convert the 0-based index to a 1-based position.
            position = i + 1

            # Add the character's reverse value multiplied
            # by its position to the total.
            total += reverse_value * position

        # Return the reverse degree of the string.
        return total