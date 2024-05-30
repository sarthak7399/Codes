# https://www.geeksforgeeks.org/problems/find-number-of-times-a-string-occurs-as-a-subsequence

# Example 1:
# Input:
# s1 = geeksforgeeks
# s2 = gks
# Output:
# 4
# Explaination: 
# We can pick characters from s1 as a subsequence from indices {0,3,4}, {0,3,12}, {0,11,12} and {8,11,12}.So total 4 subsequences of s1 that are equal to s2.

class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        MOD = int(1e9 + 7)
        m = len(s1)
        n = len(s2)
        
        # Initialize dp array
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: any s1 can form an empty s2
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
                else:
                    dp[i][j] = dp[i - 1][j] % MOD
        
        return dp[m][n]
