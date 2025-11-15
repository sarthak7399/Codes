# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

# Example 2:
# Input: s = "101101"
# Output: 16
# Explanation:
# The substrings with non-dominant ones are shown in the table below.
# Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.
# i	j	    s[i..j] 	Number of Zeros	Number of Ones
# 4	4	        0	            1           0
# 1	1	        0	            1           0
# 1	4	        0110      	    2	        2
# 0	4	        10110	        2	        3
# 1	5	        01101	        2	        3

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        # dp[i] stores the nearest index < i where s[index] == '0'
        # If s[i-1] is '0', dp[i] = i-1 , else dp[i] = dp[i-1]
        dp = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == '0':
                dp[i + 1] = i
            else:
                dp[i + 1] = dp[i]

        res = 0

        # Iterate through each ending index i
        for i in range(1, n + 1):
            # cnt0 = number of zeros included so far (we add zeros going backwards)
            cnt0 = 1 if s[i - 1] == '0' else 0
            j = i

            # Continue going backwards while cnt0^2 doesn't exceed string length
            while j > 0 and cnt0 * cnt0 <= n:

                # Number of ones between dp[j] and i
                # (i - dp[j]) is total length from dp[j]+1 to i
                cnt1 = (i - dp[j]) - cnt0

                # Check if condition cnt0^2 <= cnt1 holds
                if cnt0 * cnt0 <= cnt1:
                    # Count valid substrings ending at i for this j-range
                    res += min(j - dp[j], cnt1 - cnt0 * cnt0 + 1)

                # Jump to previous zero position and increase zero count
                j = dp[j]
                cnt0 += 1

        return res
