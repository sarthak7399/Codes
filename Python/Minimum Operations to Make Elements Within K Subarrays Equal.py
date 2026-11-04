# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

# Example 1:
# Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2
# Output: 8
# Explanation:
# Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
# Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
# Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression: map each distinct value to a sorted rank.
        vals = sorted(set(nums))
        m = len(vals)
        pos_of = {v: i + 1 for i, v in enumerate(vals)}
        rk = [pos_of[v] for v in nums]

        # Fenwick trees to maintain the frequency and sum of values
        # in the current sliding window.
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        # Find the largest power of 2 not greater than m.
        # This is used for binary lifting on the Fenwick tree.
        top = 1
        while top * 2 <= m:
            top *= 2

        # Position of the lower median in a window of size x.
        need = (x + 1) // 2

        # Number of windows of size x.
        w = n - x + 1
        cost = [0] * w

        # Maintain the sum of elements in the current window.
        total = 0

        # Slide a window of size x across the array.
        for i in range(n):
            v = nums[i]
            total += v

            # Insert the current value into both Fenwick trees.
            p = rk[i]
            while p <= m:
                cnt[p] += 1
                sm[p] += v
                p += p & -p

            # Remove the element that falls outside the window.
            if i >= x:
                u = nums[i - x]
                total -= u
                p = rk[i - x]
                while p <= m:
                    cnt[p] -= 1
                    sm[p] -= u
                    p += p & -p

            # Once the window reaches size x, calculate its minimum
            # cost to make all elements equal to its median.
            if i >= x - 1:
                # Find the rank of the lower median using Fenwick tree
                # binary lifting, while also calculating the sum of
                # all elements strictly smaller than the median.
                pos = 0
                rem = need
                s0 = 0
                pw = top

                while pw:
                    nxt = pos + pw

                    # Skip this Fenwick tree block if its frequency
                    # is smaller than the remaining median position.
                    if nxt <= m and cnt[nxt] < rem:
                        pos = nxt
                        rem -= cnt[nxt]
                        s0 += sm[nxt]

                    pw >>= 1

                # Retrieve the median value.
                med = vals[pos]

                # Number of elements at or below the median.
                c0 = need - rem

                # Calculate the cost of converting the entire window
                # into the median using absolute differences.
                # s0 is the sum of elements smaller than the median.
                cost[i - x + 1] = med * c0 - s0 + (total - s0) - med * (x - c0)

        # Large value representing an impossible or uncomputed state.
        INF = 1 << 60

        # prev[i] stores the minimum cost of selecting the required
        # number of non-overlapping windows from the first i elements.
        prev = [0] * (n + 1)

        # Perform DP for selecting exactly k non-overlapping windows.
        for _ in range(k):
            cur = [INF] * (n + 1)

            for i in range(x, n + 1):
                # Option 1: Do not select a window ending at position i.
                a = cur[i - 1]

                # Option 2: Select the window of size x ending at i.
                # Add its conversion cost to the previous DP state,
                # ensuring the selected windows do not overlap.
                b = prev[i - x] + cost[i - x]

                # Store the minimum cost between the two choices.
                cur[i] = a if a < b else b

            # Move to the next DP iteration.
            prev = cur

        # Return the minimum cost of selecting exactly k non-overlapping windows.
        return prev[n]