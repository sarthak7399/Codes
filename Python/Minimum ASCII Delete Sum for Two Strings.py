# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # m = length of s1, n = length of s2
        m, n = len(s1), len(s2)

        # dp[i][j] = maximum ASCII sum of common subsequence
        # between s1[i:] and s2[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill DP from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # If characters match, take this character and move diagonally
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i + 1][j + 1]
                else:
                    # Otherwise, skip one character from either string
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # Total ASCII sum of both strings
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)

        # Remove twice the common kept part to get minimum deletion cost
        return total - 2 * dp[0][0]
