# https://www.geeksforgeeks.org/problems/trail-of-ones3242/

# Example 1:
# Input: n = 2
# Output: 1
# Explanation:
# There are 4 strings of length 2, the strings 
# are 00, 01, 10, and 11. Only the string 11 has consecutive 1's.

class Solution:
    def numberOfConsecutiveOnes (ob,n):
        MOD = 1000000007

        # Edge case
        if n == 0:
            return 0

        # Total number of binary strings of length n
        total_binary_strings = pow(2, n, MOD)

        # DP array to store the number of valid strings without consecutive 1's
        if n == 1:
            return 0  # As there are no consecutive 1s in a single bit
        
        dp = [0] * (n + 1)
        dp[0] = 1  # There's 1 way to arrange a string of length 0 (empty string)
        dp[1] = 2  # "0" and "1"

        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD

        # Number of binary strings with at least one consecutive 1
        result = (total_binary_strings - dp[n]) % MOD
        
        # In case the result is negative
        if result < 0:
            result += MOD
        
        return result