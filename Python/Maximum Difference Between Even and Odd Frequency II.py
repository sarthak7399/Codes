# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

# Example 1:
# Input: s = "12233", k = 4
# Output: -1
# Explanation:
# For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

from typing import Counter, List

class Solution:
    # Helper function to calculate the max difference between digit `a` and `b`
    def maxDfromAtoB(self, a: int, b: int, k: int, n: int, freq: List[List[int]]) -> int:
        cnt = float('-inf')  # Initialize the result with negative infinity
        MOD = 10 ** 8        # A large number to act as initial minimum
        minFreq = [[MOD, MOD], [MOD, MOD]]  # Tracks min (a_count - b_count) for even/odd parity combos
        freqA = 0
        freqB = 0
        prevA = 0
        prevB = 0
        l = 0  # Left pointer for sliding window

        for r in range(k - 1, n):  # Sliding window from size k to n
            freqA = freq[a][r + 1]  # Total count of digit a up to position r
            freqB = freq[b][r + 1]  # Total count of digit b up to position r

            # Move left pointer to ensure we have at least 2 of digit b in the window
            while r - l + 1 >= k and freqB - prevB >= 2:
                # Update minFreq for the current parity combination
                minFreq[prevA & 1][prevB & 1] = min(minFreq[prevA & 1][prevB & 1], prevA - prevB)
                prevA = freq[a][l + 1]
                prevB = freq[b][l + 1]
                l += 1

            # Try to maximize (freqA - freqB - minFreq) based on parity constraint
            cnt = max(cnt, freqA - freqB - minFreq[1 - (freqA & 1)][freqB & 1])

        return cnt

    # Main function to compute the maximum difference between any two digits
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        freq = [[0] * (n + 1) for _ in range(5)]  # freq[d][i] = frequency of digit d from 0 to i-1
        conter = Counter(s)  # Counts frequency of each digit in the full string

        # Precompute prefix sums for each digit
        for i in range(n):
            for d in range(5):
                freq[d][i + 1] = freq[d][i]
            freq[int(s[i])][i + 1] += 1

        ans = float('-inf')  # Initialize max answer

        # Try all combinations of digits a and b
        for a in range(5):
            if freq[a][n] == 0:  # Skip if digit a is not present in the string
                continue
            for b in range(5):
                if a == b or freq[b][n] == 0:  # Skip if same digit or b is not present
                    continue
                # Compute max difference of a - b for substrings of at least length k
                ans = max(ans, self.maxDfromAtoB(a, b, k, n, freq))

        return ans
