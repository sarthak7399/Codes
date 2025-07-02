# https://leetcode.com/problems/find-the-original-typed-string-ii/

# Example 1:
# Input: word = "aabbccdd", k = 7
# Output: 5
# Explanation:
# The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

MOD = 10**9 + 7  # Large prime number for modulo to prevent overflow

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # Step 1: Group consecutive characters into blocks and get their lengths
        groups = self.getConsecutiveLetters(word)

        # Step 2: Calculate total combinations by multiplying group sizes
        # Each group of length `g` allows `g` ways to select a character
        totalCombinations = 1
        for g in groups:
            totalCombinations = (totalCombinations * g) % MOD

        # Step 3: If required length k is less than or equal to number of groups,
        # we can always form such a string with one character per group
        if k <= len(groups):
            return totalCombinations

        # Step 4: Initialize dynamic programming (DP) array
        # dp[i] = number of ways to form a string of length i using prefixes of groups
        dp = [0] * k
        dp[0] = 1  # Base case: one way to make empty string of length 0

        # Step 5: For each group, update DP table using sliding window
        for i in range(len(groups)):
            group = groups[i]
            new_dp = [0] * k
            window_sum = 0

            # Step 5.1: Use sliding window to calculate number of ways for each length j
            for j in range(i, k):
                new_dp[j] = (new_dp[j] + window_sum) % MOD
                window_sum = (window_sum + dp[j]) % MOD

                # Step 5.2: Shrink the window if its size exceeds group limit
                if j >= group:
                    window_sum = (window_sum - dp[j - group] + MOD) % MOD

            dp = new_dp  # Move to next group

        # Step 6: Sum up all possible invalid combinations (length < k)
        invalid = sum(dp) % MOD

        # Step 7: Valid combinations = totalCombinations - invalid combinations
        return (totalCombinations - invalid + MOD) % MOD

    def getConsecutiveLetters(self, word: str) -> list:
        # Helper to convert word into lengths of consecutive identical characters
        if not word:
            return []
        
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  # Add the last group
        return groups
