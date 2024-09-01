# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

# Example 1:
# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixXor = [0] * (n + 1)  # Array to store prefix XOR values
        
        # Compute prefix XOR values
        for i in range(n):
            prefixXor[i + 1] = prefixXor[i] ^ arr[i]
        
        tripletCount = 0  # Initialize count of triplets

        # Iterate through the array to find valid triplets
        for i in range(n):
            for k in range(i + 1, n):
                # If prefixXor[i] == prefixXor[k + 1], it means arr[i] ^ ... ^ arr[k] == 0
                if prefixXor[i] == prefixXor[k + 1]:
                    tripletCount += (k - i)  # Count the number of valid triplets

        return tripletCount
