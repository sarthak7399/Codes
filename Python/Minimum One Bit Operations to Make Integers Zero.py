# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

# Example 2:
# Input: n = 6
# Output: 4
# Explanation: The binary representation of 6 is "110".
# "110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
# "010" -> "011" with the 1st operation.
# "011" -> "001" with the 2nd operation since the 0th bit is 1.
# "001" -> "000" with the 1st operation.

from math import log2

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Recursive helper function using Gray code pattern
        def f(n):
            if n <= 1:
                return n
            k = int(log2(n))  # Find highest set bit position
            # Compute operations using bit manipulation and recursion
            return (1 << (k + 1)) - 1 - f(n ^ (1 << k))
        
        return f(n)
