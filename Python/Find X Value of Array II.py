# https://leetcode.com/problems/find-x-value-of-array-ii/

# Example 1:
# Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
# Output: [2,2,2]
# Explanation:
# For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
# Remove the suffix [2, 4, 5]. nums becomes [1, 2].
# Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
# For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
# Remove the empty suffix. nums becomes [3, 5].
# Remove the suffix [5]. nums becomes [3].
# For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
# Remove the suffix [2, 2, 3, 5]. nums becomes [1].
# Remove the suffix [3, 5]. nums becomes [1, 2, 2].

from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        # Store the length of the array.
        n = len(nums)

        # Only the remainder modulo k is relevant for products.
        nums = [x % k for x in nums]

        # Segment tree storing the product modulo k for each node.
        tree_prod = [0] * (4 * n)

        # tree_remain[node][r] stores the number of subarrays
        # in this segment whose product modulo k equals r.
        tree_remain = [[0] * k for _ in range(4 * n)]

        def merge(left_prod, left_remain, right_prod, right_remain):
            # Product of the complete combined segment.
            prod = (left_prod * right_prod) % k

            # Start with all subarrays completely inside the left segment.
            remain = list(left_remain)

            # Combine subarrays that cross from the left segment
            # into the right segment.
            #
            # A subarray ending in the right segment gets its product
            # multiplied by the product of the complete left segment.
            for i in range(k):
                remain[(i * left_prod) % k] += right_remain[i]

            return prod, remain

        def build(node, l, r):
            # Leaf node represents a single array element.
            if l == r:
                val = nums[l]

                # Product of a single element.
                tree_prod[node] = val

                # Exactly one subarray exists: the element itself.
                rem = [0] * k
                rem[val] = 1

                tree_remain[node] = rem
                return

            # Split the current segment into two halves.
            mid = (l + r) // 2

            # Build the left child.
            build(2 * node, l, mid)

            # Build the right child.
            build(2 * node + 1, mid + 1, r)

            # Get information from both children.
            p_l, rem_l = tree_prod[2 * node], tree_remain[2 * node]
            p_r, rem_r = tree_prod[2 * node + 1], tree_remain[2 * node + 1]

            # Merge both halves into the current node.
            tree_prod[node], tree_remain[node] = merge(
                p_l, rem_l, p_r, rem_r
            )

        def update(node, l, r, idx, val):
            # Reached the element that needs to be updated.
            if l == r:
                tree_prod[node] = val

                # Reset the remainder counts for this leaf.
                rem = [0] * k
                rem[val] = 1
                tree_remain[node] = rem
                return

            # Split the current segment.
            mid = (l + r) // 2

            # Update the appropriate child.
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)

            # Get updated information from both children.
            p_l, rem_l = tree_prod[2 * node], tree_remain[2 * node]
            p_r, rem_r = tree_prod[2 * node + 1], tree_remain[2 * node + 1]

            # Recalculate the current node after the update.
            tree_prod[node], tree_remain[node] = merge(
                p_l, rem_l, p_r, rem_r
            )

        def query(node, l, r, ql, qr):
            # If the current segment is completely inside the query range,
            # return its stored product and remainder counts.
            if ql <= l and r <= qr:
                return tree_prod[node], tree_remain[node]

            # Find the middle of the current segment.
            mid = (l + r) // 2

            # Query only the left child.
            if qr <= mid:
                return query(2 * node, l, mid, ql, qr)

            # Query only the right child.
            elif ql > mid:
                return query(2 * node + 1, mid + 1, r, ql, qr)

            # The query range spans both children.
            else:
                p_l, rem_l = query(2 * node, l, mid, ql, qr)
                p_r, rem_r = query(2 * node + 1, mid + 1, r, ql, qr)

                # Merge the results from both parts.
                return merge(p_l, rem_l, p_r, rem_r)

        # Build the segment tree using the initial array.
        build(1, 0, n - 1)

        # Store answers for all queries.
        ans = []

        # Process each query.
        for index_i, value_i, start_i, xi in queries:
            # Convert the updated value to its remainder modulo k.
            v = value_i % k

            # Update the specified index.
            update(1, 0, n - 1, index_i, v)

            # Query the range [start_i, n - 1].
            # We only need the remainder counts, not the total product.
            _, rem = query(1, 0, n - 1, start_i, n - 1)

            # Add the number of subarrays whose product modulo k
            # equals the required remainder xi.
            ans.append(rem[xi])

        # Return answers for all queries.
        return ans