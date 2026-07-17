# https://leetcode.com/problems/sorted-gcd-pair-queries/

# Example 1:
# Input: nums = [2,3,4], queries = [0,2,2]
# Output: [1,2,2]
# Explanation:
# gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].
# After sorting in ascending order, gcdPairs = [1, 1, 2].
# So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].

from bisect import bisect_right
from itertools import accumulate
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Maximum value in the array
        mx = max(nums)

        # freq[x] = frequency of value x
        freq = [0] * (mx + 1)
        for v in nums:
            freq[v] += 1

        # g[d] = number of pairs whose GCD is exactly d
        g = [0] * (mx + 1)

        # Compute pair counts for every possible GCD
        # using inclusion-exclusion
        for d in range(mx, 0, -1):

            # Number of array elements divisible by d
            m = 0

            for k in range(d, mx + 1, d):
                m += freq[k]

                # Remove pairs already counted for
                # larger multiples of d (2d, 3d, ...)
                # At k == d, g[d] is still 0.
                g[d] -= g[k]

            # Total pairs whose values are divisible by d
            total_pairs = m * (m - 1) // 2

            # After removing larger multiples,
            # g[d] stores pairs with GCD exactly d.
            g[d] += total_pairs

        # Prefix sums:
        # s[d] = number of pairs whose GCD is <= d
        s = list(accumulate(g))

        # For each query q, find the smallest GCD such that
        # more than q pairs have GCD <= that value.
        return [bisect_right(s, q) for q in queries]