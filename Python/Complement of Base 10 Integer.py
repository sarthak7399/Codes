# https://leetcode.com/problems/complement-of-base-10-integer/

# Example 1:
# Input: n = 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        # Special case: complement of 0 is 1
        # Because binary of 0 is "0", flipping it gives "1"
        if n == 0:
            return 1
        
        # Find the number of bits required to represent n in binary
        # Example: n = 5 (101) -> bit_length = 3
        bit_length = n.bit_length()
        
        # Create a mask having all bits set to 1 for the same length
        # Example: bit_length = 3 -> mask = 111 (binary) = 7
        # (1 << bit_length) shifts 1 left by bit_length positions
        # subtracting 1 converts it into all 1s
        mask = (1 << bit_length) - 1
        
        # XOR n with mask to flip all bits
        # Example: 101 ^ 111 = 010
        return n ^ mask