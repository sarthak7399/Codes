# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

# Example 1:
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        ans = []  # Stores prefix common counts

        # seen[x]:
        # 0 → not seen yet
        # 1 → seen once (either in A or B)
        # 2 → seen in both arrays (counted as common)
        seen = [0] * (n + 1)

        common = 0  # Count of common elements so far
        
        # Traverse prefixes of both arrays
        for i in range(n):

            # Process element from A
            if seen[A[i]] == 0:
                # First occurrence
                seen[A[i]] = 1

            elif seen[A[i]] == 1:
                # Element now appears in both arrays
                common += 1

            # Process element from B
            if seen[B[i]] == 0:
                # First occurrence
                seen[B[i]] = 1

            elif seen[B[i]] == 1:
                # Element now appears in both arrays
                common += 1

            # Store current count of common elements
            ans.append(common)

        return ans