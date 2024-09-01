# https://leetcode.com/problems/get-equal-substrings-within-budget/

# Example 1:
# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)  # Length of the strings s and t
        start_index = 0  # Start index of the current window
        current_cost = 0  # Current cost of transforming substring s[start_index:end] to t[start_index:end]
        max_length = 0  # Maximum length of the substring found that meets the cost constraint

        # Iterate over each character in the string
        for end_index in range(n):
            # Add the cost of transforming the current character
            current_cost += abs(ord(s[end_index]) - ord(t[end_index]))

            # If the current cost exceeds maxCost, move the start index to the right
            while current_cost > maxCost:
                current_cost -= abs(ord(s[start_index]) - ord(t[start_index]))
                start_index += 1

            # Update the maximum length of the valid substring found
            max_length = max(max_length, end_index - start_index + 1)
        
        return max_length  # Return the maximum length of the valid substring
