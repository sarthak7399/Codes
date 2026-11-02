# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

# Example 1:
# Input: nums = [1,2,1]
# Output: 15
# Explanation: Six possible subarrays are:
# [1]: 1 distinct value
# [2]: 1 distinct value
# [1]: 1 distinct value
# [1,2]: 2 distinct values
# [2,1]: 2 distinct values
# [1,2,1]: 2 distinct values
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # Modulo value to keep calculations within limits.
        MOD = 10**9 + 7

        # Length of the input array.
        n = len(nums)

        # Segment tree arrays:
        # sum_[v] = sum of distinct counts over the segment.
        # sumsq[v] = sum of squared distinct counts over the segment.
        # lazy[v] = pending increment to apply to the segment.
        sum_ = [0] * (4 * n)
        sumsq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(v, tl, tr):
            # Propagate a pending update to the children.
            # A leaf node has no children to update.
            if lazy[v] != 0 and tl != tr:
                mid = (tl + tr) // 2

                # Calculate the lengths of the left and right segments.
                llen = mid - tl + 1
                rlen = tr - mid

                # Increment that must be applied to both children.
                add = lazy[v]

                # Update the left child's sum of squares.
                # (x + add)^2 = x^2 + 2 * add * x + add^2.
                sumsq[v * 2] = (
                    sumsq[v * 2]
                    + 2 * add * sum_[v * 2]
                    + add * add % MOD * llen
                ) % MOD

                # Update the left child's sum and lazy value.
                sum_[v * 2] = (sum_[v * 2] + add * llen) % MOD
                lazy[v * 2] = (lazy[v * 2] + add) % MOD

                # Update the right child's sum of squares.
                sumsq[v * 2 + 1] = (
                    sumsq[v * 2 + 1]
                    + 2 * add * sum_[v * 2 + 1]
                    + add * add % MOD * rlen
                ) % MOD

                # Update the right child's sum and lazy value.
                sum_[v * 2 + 1] = (sum_[v * 2 + 1] + add * rlen) % MOD
                lazy[v * 2 + 1] = (lazy[v * 2 + 1] + add) % MOD

                # Clear the pending update from the current node.
                lazy[v] = 0

        def update(v, tl, tr, l, r, add):
            # No overlap between the current segment and update range.
            if l > r:
                return

            # If the current segment fully matches the update range,
            # apply the increment without visiting its children.
            if l == tl and r == tr:
                length = tr - tl + 1

                # Update the sum of squares using the square expansion formula.
                sumsq[v] = (
                    sumsq[v] + 2 * add * sum_[v]
                    + add * add % MOD * length
                ) % MOD

                # Update the sum and record the lazy increment.
                sum_[v] = (sum_[v] + add * length) % MOD
                lazy[v] = (lazy[v] + add) % MOD
                return

            # Apply any pending updates before descending.
            push(v, tl, tr)
            mid = (tl + tr) // 2

            # Update the overlapping portion of the left child.
            update(v * 2, tl, mid, l, min(r, mid), add)

            # Update the overlapping portion of the right child.
            update(v * 2 + 1, mid + 1, tr, max(l, mid + 1), r, add)

            # Recalculate the parent values from its children.
            sum_[v] = (sum_[v * 2] + sum_[v * 2 + 1]) % MOD
            sumsq[v] = (sumsq[v * 2] + sumsq[v * 2 + 1]) % MOD

        def query(v, tl, tr, l, r):
            # Return 0 if the query range is empty.
            if l > r:
                return 0

            # If the current segment matches the query range,
            # return its stored sum of squares.
            if l == tl and r == tr:
                return sumsq[v]

            # Propagate pending updates before querying children.
            push(v, tl, tr)
            mid = (tl + tr) // 2

            # Query both children and combine their results.
            return (
                query(v * 2, tl, mid, l, min(r, mid))
                + query(v * 2 + 1, mid + 1, tr, max(l, mid + 1), r)
            ) % MOD

        # Store the most recent index of each value.
        # -1 means the value has not appeared before.
        last = [-1] * 100001

        # Sum of squared distinct counts for all subarrays processed so far.
        ans = 0

        # Treat each index r as the right endpoint of new subarrays.
        for r in range(n):
            # Find the previous occurrence of nums[r].
            prv = last[nums[r]]

            # For subarrays starting after prv and ending before r,
            # nums[r] introduces one additional distinct value.
            if prv + 1 <= r - 1:
                update(1, 0, n - 1, prv + 1, r - 1, 1)

            # The subarray [r, r] contains one distinct value.
            # Initialize its distinct count by incrementing this position.
            update(1, 0, n - 1, r, r, 1)

            # Add the squared distinct counts of all subarrays ending at r.
            ans = (ans + query(1, 0, n - 1, 0, r)) % MOD

            # Update the latest occurrence of the current value.
            last[nums[r]] = r

        # Return the total modulo MOD.
        return ans