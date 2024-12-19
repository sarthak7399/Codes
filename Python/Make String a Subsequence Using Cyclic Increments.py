# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

# Example 1:
# Input: str1 = "abc", str2 = "ad"
# Output: true
# Explanation: Select index 2 in str1.
# Increment str1[2] to become 'd'. 
# Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.

class Solution:
    def canMakeSubsequence(self, source: str, target: str) -> bool:
        # Initialize index for target and find the length of the target string
        targetIdx, targetLen = 0, len(target)
        
        # Iterate through each character in the source string
        for currChar in source:
            # Check if there are still characters left in the target string to match
            # and if the current character from source matches the target character
            # either directly or after incrementing it (circular increment in alphabet)
            if targetIdx < targetLen and (ord(target[targetIdx]) - ord(currChar)) % 26 < 2:
                # Move to the next character in the target string since a match is found
                targetIdx += 1
        
        # If we have matched all characters in the target string, return True
        # Otherwise, return False
        return targetIdx == targetLen
