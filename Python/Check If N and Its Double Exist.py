# https://leetcode.com/problems/check-if-n-and-its-double-exist/

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}  # Dictionary to store elements

        for num in arr:  # Iterate over the array
            # Check if 2 * num or num / 2 exists in the dictionary
            if (2 * num in seen) or (num % 2 == 0 and num // 2 in seen):
                return True  # Return true if the condition is met
            # Add the current number to the dictionary
            seen[num] = seen.get(num, 0) + 1

        return False  # Return false if no such pair exists