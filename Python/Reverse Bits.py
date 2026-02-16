# https://leetcode.com/problems/reverse-bits/

# Example 1:
# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # will store the reversed bits
        
        # Loop exactly 32 times (because integer is 32-bit)
        for i in range(32):
            
            # Shift result left to make space for next bit
            res = res << 1
            
            # Take last bit of n using AND with 1
            # and add it to result
            res = res | (n & 1)
            
            # Shift n right to process next bit
            n >>= 1
        
        return res
