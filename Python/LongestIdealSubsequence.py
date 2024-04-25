# https://leetcode.com/problems/longest-ideal-subsequence/

# Example 1:
# Input: s = "acfgbd", k = 2
# Output: 4
# Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
# Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Initialize an array to store the length of ideal strings ending at each character index
        lengths = [0] * 128
        
        # Iterate through each character in the string
        for c in s:
            i = ord(c)  # Get the ASCII value of the character
            # Calculate the length of the ideal string ending at the current character index
            # by taking the maximum length from the previous k characters to the next k characters
            lengths[i] = max(lengths[i - k : i + k + 1]) + 1
        
        # Return the maximum length of ideal strings
        return max(lengths)
