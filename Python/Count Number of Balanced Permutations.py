# https://leetcode.com/problems/count-number-of-balanced-permutations/

# Example 1:
# Input: num = "123"
# Output: 2
# Explanation:
# The distinct permutations of num are "123", "132", "213", "231", "312" and "321".
# Among them, "132" and "231" are balanced. Thus, the answer is 2.

MOD = 10**9 + 7  # A large prime for modulo operations to avoid overflow

class Solution:
    def __init__(self):
        # Arrays for precomputed factorials, modular inverses, and inverse factorials
        self.fact = []
        self.inv = []
        self.invFact = []

    def precompute(self, n):
        # Precompute factorials, modular inverses, and inverse factorials up to n
        self.fact = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        self.invFact = [1] * (n + 1)

        # Compute factorials: fact[i] = i!
        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % MOD

        # Compute modular inverses using Fermat's Little Theorem:
        # inv[i] = modular inverse of i under MOD
        for i in range(2, n + 1):
            self.inv[i] = MOD - MOD // i * self.inv[MOD % i] % MOD

        # Compute inverse factorials
        for i in range(1, n + 1):
            self.invFact[i] = self.invFact[i - 1] * self.inv[i] % MOD

    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        digit_values = [int(c) for c in num]  # Convert each character to an integer digit
        total_sum = sum(digit_values)        # Sum of all digits

        # If total sum is odd, it can’t be evenly split into two equal halves
        if total_sum % 2 == 1:
            return 0

        # Precompute factorials and inverses for up to length n
        self.precompute(n)

        half_sum = total_sum // 2      # Each half of the balanced permutation must sum to this
        half_len = n // 2              # Each half must have exactly n/2 digits

        # dp[s][l] = number of ways to get sum `s` using `l` digits
        dp = [[0] * (half_len + 1) for _ in range(half_sum + 1)]
        dp[0][0] = 1  # Base case: 1 way to get sum 0 using 0 digits

        digit_count = [0] * 10  # Count occurrences of each digit 0–9

        # Count digit frequency and fill DP table
        for d in digit_values:
            digit_count[d] += 1
            for s in range(half_sum, d - 1, -1):
                for l in range(half_len, 0, -1):
                    # Add number of ways to reach sum `s` with `l` digits including digit `d`
                    dp[s][l] = (dp[s][l] + dp[s - d][l - 1]) % MOD

        # dp[half_sum][half_len] gives number of ways to choose a half with required sum and length
        res = dp[half_sum][half_len]

        # Multiply by permutations of digits in both halves (half_len! * (n - half_len)!)
        res = res * self.fact[half_len] % MOD
        res = res * self.fact[n - half_len] % MOD

        # Adjust for repeated digits using inverse factorials
        for cnt in digit_count:
            res = res * self.invFact[cnt] % MOD

        return res
