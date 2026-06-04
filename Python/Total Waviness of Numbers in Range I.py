# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

# Example 1:
# Input: num1 = 120, num2 = 130
# Output: 3
# Explanation:
# In the range [120, 130]:
# 120: middle digit 2 is a peak, waviness = 1.
# 121: middle digit 2 is a peak, waviness = 1.
# 130: middle digit 3 is a peak, waviness = 1.
# All other numbers in the range have a waviness of 0.
# Thus, total waviness is 1 + 1 + 1 = 3.

class Solution:
    MAX = 100001

    # dp[i] = waviness score of number i
    # pref[i] = prefix sum of waviness scores from 0 to i
    dp = [0] * MAX
    pref = [0] * MAX

    # Precompute waviness values for all numbers
    for i in range(100, MAX):

        # Extract last three digits
        r = i % 10              # right digit
        m = (i // 10) % 10      # middle digit
        l = (i // 100) % 10     # left digit

        # A wave occurs if middle digit is:
        # - strictly greater than both neighbors, or
        # - strictly smaller than both neighbors
        isWave = m > max(l, r) or m < min(l, r)

        # Waviness of current number =
        # waviness of prefix number (i // 10)
        # + whether current 3-digit window forms a wave
        dp[i] = dp[i // 10] + int(isWave)

        # Build prefix sum of waviness scores
        pref[i] = pref[i - 1] + dp[i]

    def totalWaviness(self, A: int, B: int) -> int:
        # Return total waviness in range [A, B]
        return self.pref[B] - self.pref[A - 1]