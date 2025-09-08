# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

# Example 1:
# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.

from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Helper function to check if a number contains digit '0'
        def check(x):
            return '0' not in str(x)

        # Try to split n into two integers i and j
        for i in range(1, n):
            j = n - i  # The second integer
            # Both i and j should not contain the digit '0'
            if check(i) and check(j):
                return [i, j]  # Return the first valid pair found
