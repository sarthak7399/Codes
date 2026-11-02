# https://leetcode.com/problems/distinct-subsequences/

# Example 1:
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # m = length of source string, n = length of target string.
        m, n = len(s), len(t)

        # dp[j] represents the number of ways to form the first j
        # characters of t using the characters processed from s.
        dp = [0] * (n + 1)

        # There is exactly one way to form an empty target:
        # choose no characters from s.
        dp[0] = 1

        # Process each character of the source string.
        for i in range(1, m + 1):

            # Traverse backwards so that dp[j - 1] still represents
            # the previous iteration and is not overwritten.
            #
            # We cannot form more than i characters of t using only
            # the first i characters of s.
            for j in range(min(i, n), 0, -1):

                # If the current characters match, every way of forming
                # t[:j - 1] can be extended to form t[:j].
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        # Return the number of distinct subsequences of s equal to t.
        return dp[n]