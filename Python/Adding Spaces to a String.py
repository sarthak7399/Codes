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
        # Initialize the starting index for slicing the string
        index = 0
        # Create an empty list to store parts of the string
        result = []

        # Iterate through each space position in the 'spaces' list
        for space in spaces:
            # Slice the string from the current index up to the current space position
            # and append it to the result list
            result.append(s[index : space])
            # Update the starting index to the current space position
            index = space

        # After processing all the spaces, append the remaining part of the string
        # from the last space position to the end of the string
        result.append(s[index :])
        
        # Join the parts in the result list with a space between them and return
        return " ".join(result)
