# https://leetcode.com/problems/partition-labels/

# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = [0] * 26  # Array to track the frequency of each character
        a = ord('a')  # Reference for converting characters to indices

        # Count occurrences of each character in the string
        for char in s:
            freq[ord(char) - a] += 1

        output = []  # List to store the partition sizes
        prev_end = 0  # Marks the end of the last partition

        # Function to check if all characters in the current partition have been used
        def is_valid(start, end):
            for i in range(start, end + 1):
                if freq[ord(s[i]) - a] != 0:  # If any character is still present later, return False
                    return False
            return True

        # Iterate through the string to determine partitions
        for i in range(len(s)):
            freq[ord(s[i]) - a] -= 1  # Decrease count as character is processed
            
            # If all characters in the current partition are fully used, finalize partition
            if is_valid(prev_end, i):
                output.append(i - prev_end + 1)  # Store partition size
                prev_end = i + 1  # Update the start of the next partition

        return output
