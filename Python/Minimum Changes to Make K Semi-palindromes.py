# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

# Example 1:
# Input: s = "abcac", k = 2
# Output: 1
# Explanation: Divide s into "ab" and "cac". "cac" is already semi-palindrome. Change "ab" to "aa", it becomes semi-palindrome with d = 1.

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9

        # cost[i][j] stores the minimum changes required to make
        # the substring s[i:j+1] satisfy the required condition
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF

                # Try all possible divisors of the substring length
                for d in range(1, L):
                    # The substring length must be divisible by d
                    if L % d != 0:
                        continue

                    cur = 0
                    m = L // d

                    # Divide the substring into d groups
                    # Each group contains characters at a distance of d
                    for r in range(d):
                        # Compare symmetric characters in each group
                        # to calculate the required changes
                        for t in range(m // 2):
                            if s[i + r + t * d] != s[i + r + (m - 1 - t) * d]:
                                cur += 1

                    # Keep the minimum changes among all valid divisors
                    best = min(best, cur)

                cost[i][j] = best

        # dp[i][p] represents the minimum changes needed to divide
        # the first i characters into exactly p valid substrings
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        # Base case: zero characters divided into zero parts
        dp[0][0] = 0

        # Consider prefixes of different lengths
        for i in range(1, n + 1):
            # Try forming exactly p substrings
            for p in range(1, k + 1):
                # Try every possible starting position of the last substring
                for prev in range(i - 1):
                    # Ensure at least two characters are present in the last substring
                    # and both previous DP state and substring cost are valid
                    if prev <= i - 2 and dp[prev][p - 1] != INF and cost[prev][i - 1] != INF:

                        # Transition: previous minimum cost + cost of the last substring
                        dp[i][p] = min(
                            dp[i][p],
                            dp[prev][p - 1] + cost[prev][i - 1]
                        )

        # Return the minimum changes needed to divide the entire string into k parts
        return dp[n][k]