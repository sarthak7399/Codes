# https://leetcode.com/problems/power-of-two/

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A number is a power of two if:
        # 1. It is positive (n > 0)
        # 2. It has only one bit set in its binary representation.
        #    The trick: n & (n - 1) removes the lowest set bit.
        #    If the result is 0, then n had exactly one set bit → power of two.
        return n > 0 and (n & (n - 1)) == 0
