# https://leetcode.com/problems/range-product-queries-of-powers/

# Example 1:
# Input: n = 15, queries = [[0,1],[2,2],[0,3]]
# Output: [2,4,64]
# Explanation:
# For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
# Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
# Answer to 2nd query: powers[2] = 4.
# Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
# Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.

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
