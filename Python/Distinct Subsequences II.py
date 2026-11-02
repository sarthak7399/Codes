# https://leetcode.com/problems/distinct-subsequences-ii/

# Example 1:
# Input: s = "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

class Solution:
    def distinctSubseqII(self, s):
        # Length of the input string.
        n = len(s)

        # Modulo required to prevent the result from becoming too large.
        MOD = 10**9 + 7

        # dp[i] represents the number of distinct non-empty subsequences
        # whose last selected character is s[i].
        dp = [1] * n

        # Stores the total number of distinct non-empty subsequences.
        result = 0

        # Process every character as the last character of a subsequence.
        for i in range(n):

            # Try appending s[i] to subsequences ending at earlier indices.
            for j in range(i):

                # Append only if the previous subsequence does not already
                # end with the same character. This avoids counting duplicate
                # subsequences ending with the same character.
                if s[i] != s[j]:
                    dp[i] = (dp[i] + dp[j]) % MOD

            # Add all distinct subsequences ending at index i
            # to the overall answer.
            result = (result + dp[i]) % MOD

        # Return the total number of distinct non-empty subsequences.
        return result