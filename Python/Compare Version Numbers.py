# https://leetcode.com/problems/compare-version-numbers/

# Example 1:
# Input: version1 = "1.2", version2 = "1.10"
# Output: -1
# Explanation:
# version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split versions by '.' and convert each part to integer
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        # Find the longer length (since versions can have unequal parts)
        n = max(len(v1), len(v2))
        
        # Compare part by part
        for i in range(n):
            # Get ith part of each version, default to 0 if index out of range
            num1 = v1[i] if i < len(v1) else 0
            num2 = v2[i] if i < len(v2) else 0
            
            # Compare current revision
            if num1 < num2:
                return -1   # version1 is smaller
            if num1 > num2:
                return 1    # version1 is larger
        
        # All parts are equal
        return 0
