# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

# Example 1:
# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: We can do the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
# - Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        # Strings to store characters at even and odd indices separately
        even1, odd1 = "", ""
        even2, odd2 = "", ""
        
        # Traverse both strings
        for i in range(len(s1)):
            
            if i % 2 == 0:
                # Even index characters
                even1 += s1[i]
                even2 += s2[i]
            else:
                # Odd index characters
                odd1 += s1[i]
                odd2 += s2[i]
        
        # Sort characters at even indices
        even1 = sorted(even1)
        even2 = sorted(even2)
        
        # Sort characters at odd indices
        odd1 = sorted(odd1)
        odd2 = sorted(odd2)

        # If both even and odd groups match → strings can be made equal
        return even1 == even2 and odd1 == odd2