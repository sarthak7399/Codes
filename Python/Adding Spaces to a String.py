# https://leetcode.com/problems/adding-spaces-to-a-string/

# Example 1:
# Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
# Output: "Leetcode Helps Me Learn"
# Explanation: 
# The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
# We then place spaces before those characters.

from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Initialize two pointers: 'i' for the string 's' and 'j' for the 'spaces' list.
        i, j = 0, 0
        # Create an empty list to build the result string efficiently.
        res = []

        # Traverse through the string 's' and 'spaces' simultaneously.
        while i < len(s) and j < len(spaces):
            # If the current index in 's' is before the next space position,
            # append the character to the result list.
            if i < spaces[j]:
                res.append(s[i])
                i += 1
            else:
                # If the current index matches the next space position,
                # append a space to the result and move to the next space index.
                res.append(" ")
                j += 1

        # If there are remaining characters in 's' after processing all spaces,
        # append them to the result.
        if i < len(s):
            res.append(s[i:])  # Use slicing to add all remaining characters.
        
        # Combine the list elements into a single string and return it.
        return "".join(res)
