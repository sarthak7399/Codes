# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

# Example 1:
# Input: nums1 = [2,5], nums2 = [3,4], k = 2
# Output: 8
# Explanation: The 2 smallest products are:
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# The 2nd smallest product is 8.

from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def kthSmallestProduct(self, n1: List[int], n2: List[int], k: int) -> int:
        # Helper function to count how many products are <= x
        def cnt(x):
            c = 0
            for a in n1:
                if a > 0:
                    # If a > 0, count how many b in n2 such that a * b <= x
                    c += bisect_right(n2, x // a)
                elif a < 0:
                    # If a < 0, need to find how many b such that a * b <= x
                    # Which becomes b >= ceil(x / a)
                    t = x // a + (1 if x % a else 0)
                    c += m2 - bisect_left(n2, t)
                else:
                    # a == 0: product is 0, which is <= x if x >= 0
                    if x >= 0:
                        c += m2
            return c

        # Ensure n1 is the smaller array to optimize performance
        if len(n1) > len(n2):
            n1, n2 = n2, n1

        m2 = len(n2)

        # Determine the minimum and maximum possible products to bound binary search
        lo = min(n1[0]*n2[0], n1[0]*n2[-1], n1[-1]*n2[0], n1[-1]*n2[-1])
        hi = max(n1[0]*n2[0], n1[0]*n2[-1], n1[-1]*n2[0], n1[-1]*n2[-1])

        # Binary search for the k-th smallest product
        while lo < hi:
            mid = (lo + hi) // 2
            if cnt(mid) >= k:
                hi = mid  # Look for smaller product
            else:
                lo = mid + 1  # Look for larger
