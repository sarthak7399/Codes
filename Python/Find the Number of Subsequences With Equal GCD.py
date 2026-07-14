# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

# Example 1:
# Input: nums = [1,2,3,4]
# Output: 10
# Explanation:
# The subsequence pairs which have the GCD of their elements equal to 1 are:
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])

from functools import lru_cache
from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        # Memoized DFS:
        # idx -> current index in nums
        # g1  -> GCD of the first subsequence
        # g2  -> GCD of the second subsequence
        @lru_cache(None)
        def solve(idx, g1, g2):

            # All elements have been processed
            if idx == n:
                # Valid only if:
                # 1. First subsequence is non-empty (g1 != 0)
                # 2. Both subsequences have the same GCD
                return 1 if g1 != 0 and g1 == g2 else 0

            # Option 1: Ignore the current element
            ans = solve(idx + 1, g1, g2)

            # Option 2: Add the current element to the first subsequence
            ng1 = nums[idx] if g1 == 0 else gcd(g1, nums[idx])
            ans = (ans + solve(idx + 1, ng1, g2)) % MOD

            # Option 3: Add the current element to the second subsequence
            ng2 = nums[idx] if g2 == 0 else gcd(g2, nums[idx])
            ans = (ans + solve(idx + 1, g1, ng2)) % MOD

            return ans

        # Start with both subsequences empty (GCD = 0)
        return solve(0, 0, 0)