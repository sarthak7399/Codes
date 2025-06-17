# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

# Example 1:
# Input: n = 3, m = 2, k = 1
# Output: 4
# Explanation:
# There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
# Hence, the answer is 4.

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7  # Modulo value for large number operations

        # Function to compute modular inverse using Fermat's Little Theorem
        def mod_inverse(x):
            return pow(x, MOD - 2, MOD)
        
        # Precompute factorials up to (n - 1)
        max_size = n
        factorial = [1] * max_size
        for i in range(1, max_size):
            factorial[i] = (factorial[i - 1] * i) % MOD
        
        # Function to compute C(a, b) % MOD (combinations)
        def nCr(a, b):
            if b < 0 or b > a:
                return 0
            return (factorial[a] * mod_inverse(factorial[b]) % MOD) * mod_inverse(factorial[a - b]) % MOD

        # Compute the combination part: choosing `k` positions to place breaks between same numbers
        combination_part = nCr(n - 1, k)

        # Compute power part: number of ways to assign `m-1` other values to remaining `n - 1 - k` slots
        power_part = pow(m - 1, n - 1 - k, MOD)

        # Total ways: multiply m choices for the first number, combinations, and power part
        return combination_part * m % MOD * power_part % MOD
