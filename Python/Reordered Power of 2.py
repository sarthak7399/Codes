# https://leetcode.com/problems/reordered-power-of-2/

# Example 1:
# Input: n = 1
# Output: true

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Helper function: returns the digits of x in sorted order as a string
        # This way, two numbers having same digits (in any order) will have the same "signature"
        def count_digits(x):
            return ''.join(sorted(str(x)))

        # Get the digit signature of the given number n
        target = count_digits(n)
        
        # Check all powers of 2 up to 2^30 (since 2^30 = 1,073,741,824 fits in 32-bit int)
        for i in range(31):
            # If any power of 2 has the same sorted digits as n, return True
            if count_digits(1 << i) == target:
                return True
        
        # If no match found, return False
        return False
