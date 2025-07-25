# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

# Example 1:
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

from typing import List 
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])

        # Precompute frequency of each character at each position in words
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1

        # DP table: dp[i][j] is the number of ways to form target[:i] using the first j columns of words
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(m + 1):
            for j in range(n):
                # Carry forward the previous ways
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD

                if i < m:  # If there's still a character in target to form
                    char_idx = ord(target[i]) - ord('a')
                    # If the current character matches, add ways
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * freq[j][char_idx]) % MOD

        return dp[m][n]