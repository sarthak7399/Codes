# https://www.geeksforgeeks.org/problems/trail-of-ones3242/

# Example 1:
# Input: n = 2
# Output: 1
# Explanation:
# There are 4 strings of length 2, the strings 
# are 00, 01, 10, and 11. Only the string 11 has consecutive 1's.

class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        MOD=1000000007
        dp=[0]*100001
        dp[2]=1
        dp[3]=3
        for i in range(3,100001):
            dp[i]=(dp[i-1]+dp[i-2]+(pow(2,i-2,MOD)))%MOD
            
        return dp[n]