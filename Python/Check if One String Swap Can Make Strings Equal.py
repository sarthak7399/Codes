# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

# Example 1:
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Checks if two strings can be made equal by swapping at most one pair of characters.

        Args:
        s1 (str): First input string.
        s2 (str): Second input string.

        Returns:
        bool: True if they can be made equal with at most one swap, False otherwise.
        """

        count = 0  # Counter to track the number of differing characters
        freq1, freq2 = [0] * 26, [0] * 26  # Frequency arrays to store character counts

        # Count the frequency of each character in both strings
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        # If character frequencies do not match, s1 and s2 can never be equal
        if freq1 != freq2:
            return False

        # Count the number of positions where s1 and s2 differ
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1

        # They can be made equal only if they differ at exactly 0 or 2 positions
        return count <= 2
