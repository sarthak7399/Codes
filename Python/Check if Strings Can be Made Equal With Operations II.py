# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

# Example 1:
# Input: s1 = "abcdba", s2 = "cabdab"
# Output: true
# Explanation: We can apply the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
# - Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
# - Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        # Frequency arrays for characters at:
        # even indices and odd indices separately
        even = [0] * 26   # for 'a' to 'z'
        odd = [0] * 26

        # Traverse both strings
        for i in range(len(s1)):

            if i % 2 == 0:
                # Even index:
                # Increase count for s1 and decrease for s2
                even[ord(s1[i]) - ord('a')] += 1
                even[ord(s2[i]) - ord('a')] -= 1
            else:
                # Odd index:
                # Increase count for s1 and decrease for s2
                odd[ord(s1[i]) - ord('a')] += 1
                odd[ord(s2[i]) - ord('a')] -= 1

        # Check if all counts are zero
        # (means both strings have identical frequency distribution)
        for i in range(26):
            if even[i] != 0 or odd[i] != 0:
                return False

        # If all frequencies match → strings can be made equal
        return True