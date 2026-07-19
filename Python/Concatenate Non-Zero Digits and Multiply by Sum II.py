# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

# Example 1:
# Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]
# Output: [12340, 4, 9]
# Explanation:
# s[0..7] = "10203004"
# x = 1234
# sum = 1 + 2 + 3 + 4 = 10
# Therefore, answer is 1234 * 10 = 12340.
# s[1..3] = "020"
# x = 2
# sum = 2
# Therefore, the answer is 2 * 2 = 4.
# s[4..6] = "300"
# x = 3
# sum = 3
# Therefore, the answer is 3 * 3 = 9.

MOD, MAX = 1000000007, 100001

# Precompute powers of 10 modulo MOD
pow = [1] * MAX
for i in range(1, MAX):
    pow[i] = (pow[i - 1] * 10) % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)

        # Prefix arrays:
        # A[i]   = sum of digits in s[0:i]
        # B[i]   = number formed by concatenating non-zero digits in s[0:i]
        #          (stored modulo MOD)
        # Len[i] = count of non-zero digits in s[0:i]
        A, B, Len = [[0] * (n + 1) for _ in range(3)]

        # Build prefix information
        for i in range(n):
            d = int(s[i])

            # Prefix sum of digits
            A[i + 1] = A[i] + d

            # Append only non-zero digits
            if d:
                B[i + 1] = (B[i] * 10 + d) % MOD
            else:
                B[i + 1] = B[i]

            # Count non-zero digits
            Len[i + 1] = Len[i] + (d > 0)

        res = []

        # Answer each query independently
        for l, r in queries:
            # Convert to half-open interval [l, r)
            r += 1

            # Remove the contribution of the prefix before l
            sub = (B[l] * pow[Len[r] - Len[l]]) % MOD

            # Number formed by non-zero digits in s[l:r]
            x = (B[r] - sub) % MOD

            # Sum of digits in s[l:r]
            digit_sum = A[r] - A[l]

            # Required answer:
            # (number after removing zeros) × (sum of digits)
            res.append((x * digit_sum) % MOD)

        return res