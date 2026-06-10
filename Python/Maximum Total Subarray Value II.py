# https://leetcode.com/problems/maximum-total-subarray-value-ii/

# Example 1:
# Input: nums = [1,3,2], k = 2
# Output: 4
# Explanation:
# One optimal approach is:
# Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
# Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.
# Adding these gives 2 + 2 = 4.

import heapq
from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Precompute floor(log2(i)) for all lengths
        # Used for O(1) Sparse Table queries
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        LOG = lg[n] + 1

        # Sparse Table for range maximum queries
        stMax = [[0] * n for _ in range(LOG)]

        # Sparse Table for range minimum queries
        stMin = [[0] * n for _ in range(LOG)]

        # Initialize level 0 (interval length = 1)
        for i in range(n):
            stMax[0][i] = nums[i]
            stMin[0][i] = nums[i]

        # Build Sparse Tables
        # st[j][i] stores answer for interval of length 2^j
        for j in range(1, LOG):

            length = 1 << j

            for i in range(n - length + 1):

                # Maximum in interval [i, i + 2^j - 1]
                stMax[j][i] = max(
                    stMax[j - 1][i],
                    stMax[j - 1][i + (1 << (j - 1))]
                )

                # Minimum in interval [i, i + 2^j - 1]
                stMin[j][i] = min(
                    stMin[j - 1][i],
                    stMin[j - 1][i + (1 << (j - 1))]
                )

        def getValue(l, r):
            """
            Returns:
                max(nums[l:r+1]) - min(nums[l:r+1])

            Uses Sparse Table for O(1) range queries.
            """

            length = r - l + 1

            # Largest power of 2 fitting inside interval
            p = lg[length]

            # Range maximum query
            mx = max(
                stMax[p][l],
                stMax[p][r - (1 << p) + 1]
            )

            # Range minimum query
            mn = min(
                stMin[p][l],
                stMin[p][r - (1 << p) + 1]
            )

            return mx - mn

        # Max heap:
        # (-value, left_index, right_index)
        pq = []

        # Initially insert all subarrays ending at n-1
        for l in range(n):
            heapq.heappush(
                pq,
                (-getValue(l, n - 1), l, n - 1)
            )

        ans = 0

        # Extract the k largest values
        while k:

            # Get current maximum value interval
            neg_val, l, r = heapq.heappop(pq)

            val = -neg_val

            # Add contribution to answer
            ans += val

            # Generate next candidate interval
            # by shrinking right endpoint
            if r > l:
                heapq.heappush(
                    pq,
                    (-getValue(l, r - 1), l, r - 1)
                )

            k -= 1

        return ans