# https://leetcode.com/problems/binary-number-with-alternating-bits/

# Example 1:
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Step 1:
        # Shift n right by 1 bit and XOR with original number.
        #
        # If bits are alternating (101010...),
        # XOR with shifted version produces all 1s.
        #
        # Example:
        # n       = 1010
        # n >> 1  = 0101
        # XOR     = 1111
        x = n ^ (n >> 1)

        # Step 2:
        # Check if x is of the form 11111... (all bits = 1)
        #
        # Property:
        # For numbers like:
        # 1      (1)
        # 3      (11)
        # 7      (111)
        # 15     (1111)
        #
        # x & (x + 1) == 0
        #
        # because:
        #   1111
        # &10000
        # -------
        #   0000
        return (x & (x + 1)) == 0
