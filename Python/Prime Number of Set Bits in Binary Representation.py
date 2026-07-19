# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

# Example 1:
# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6  -> 110 (2 set bits, 2 is prime)
# 7  -> 111 (3 set bits, 3 is prime)
# 8  -> 1000 (1 set bit, 1 is not prime)
# 9  -> 1001 (2 set bits, 2 is prime)
# 10 -> 1010 (2 set bits, 2 is prime)
# 4 numbers have a prime number of set bits.

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Predefined set of prime numbers.
        # Maximum set bits for numbers ≤ 10^6 is small (~20),
        # so we only need primes up to 19.
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        ans = 0  # stores count of valid numbers
        
        # Iterate through all numbers in the range [left, right]
        for num in range(left, right + 1):

            # Convert number to binary string and count number of '1's
            # Example: 5 -> '0b101' -> 2 set bits
            set_bits = bin(num).count('1')
            
            # If number of set bits is prime → valid number
            if set_bits in primes:
                ans += 1
        
        # Return total count
        return ans