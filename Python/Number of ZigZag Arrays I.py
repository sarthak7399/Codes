# https://leetcode.com/problems/number-of-zigzag-arrays-i/

# Example 1:
# Input: n = 3, l = 4, r = 5
# Output: 2
# Explanation:
# There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:
# [4, 5, 4]
# [5, 4, 5]​​​​​​​

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007

        # Number of distinct values available
        # in the range [l, r]
        m = r - l + 1

        # Base case:
        # For length 1, each value can form one valid array
        dp = [1] * m

        # Build DP for array lengths from 2 to n
        for _ in range(2, n + 1):

            # Reverse DP to efficiently compute transitions
            dp.reverse()

            # Running prefix sum
            pref = 0

            for i in range(m):

                # Store current value before overwriting
                old = dp[i]

                # Number of ways for current state
                # equals the sum of all previous states
                dp[i] = pref

                # Update prefix sum
                pref = (pref + old) % MOD

        # Total number of valid sequences
        ans = sum(dp) % MOD

        # Multiply by 2 to account for both zig-zag patterns:
        # increasing-decreasing-increasing...
        # decreasing-increasing-decreasing...
        return (ans * 2) % MOD