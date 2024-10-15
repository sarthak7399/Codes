# https://leetcode.com/problems/separate-black-and-white-balls/

# Example 1:
# Input: s = "101"
# Output: 1
# Explanation: We can group all the black balls to the right in the following way:
# - Swap s[0] and s[1], s = "011".
# Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.

class Solution:
    def minimumSteps(self, s: str) -> int:
        swap, black = 0, 0
        for c in s:     # Iterating through the string
            if c == "0":    # If the current character is 0
                swap += black   # Add the number of black balls to the swap variable
            else:
                black += 1      # If the current character is 1, add 1 to the black variable
        return swap