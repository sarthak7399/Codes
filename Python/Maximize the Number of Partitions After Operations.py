# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

# Example 2:
# Input: s = "aabaab", k = 3
# Output: 1
# Explanation:
# Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        a = ord('a')
        # Convert each character to a bitmask (e.g., 'a' -> 1, 'b' -> 2, etc.)
        cnt = [1 << (ord(c) - a) for c in s]

        @lru_cache(None)
        def dp(i, j, mask):
            # Base case: reached end of string
            if i == len(cnt):
                return 0

            # Add current character to current mask
            mask2 = mask | cnt[i]

            # If exceeding k unique chars, start a new partition
            if mask2.bit_count() > k:
                ans = 1 + dp(i + 1, j, cnt[i])
            else:
                ans = dp(i + 1, j, mask2)

            # If we still have the option to modify one character
            if j:
                for q in range(26):  # try replacing with any letter
                    mask2 = mask | (1 << q)
                    if mask2.bit_count() > k:
                        ans = max(ans, 1 + dp(i + 1, 0, 1 << q))
                    else:
                        ans = max(ans, dp(i + 1, 0, mask2))
            return ans

        # Add 1 to count the final partition
        return dp(0, 1, 0) + 1
