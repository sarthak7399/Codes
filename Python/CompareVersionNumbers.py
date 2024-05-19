# https://leetcode.com/problems/compare-version-numbers/

# Example 1:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

# Example 2:
# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: version1 does not specify revision 2, which means it is treated as "0".

from typing import List
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Helper function to extract each version number segment
        def extract_version(s: str, idx: int) -> List[int]:
            num = 0
            # Iterate through the string starting from the given index
            while idx < len(s):
                # Check if the current character is a dot, indicating the end of the segment
                if s[idx] == '.':
                    break
                else:
                    # Convert the character to integer and accumulate to form the segment number
                    num = num * 10 + int(s[idx])
                idx += 1
            # Return the segment number and the index of the next character
            return [num, idx+1]

        i = j = 0
        # Iterate through both version strings
        while(i < len(version1) or j < len(version2)):
            # Extract version numbers from both strings
            v1, i = extract_version(version1, i)
            v2, j = extract_version(version2, j)
            # Compare the extracted version numbers
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        # If both versions are equal, return 0
        return 0
