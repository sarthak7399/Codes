# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

# Example 1:
# Input: nums1 = [2,5], nums2 = [3,4], k = 2
# Output: 8
# Explanation: The 2 smallest products are:
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# The 2nd smallest product is 8.

import bisect

class Solution:
    # Helper function to count number of pairs (a[i], b[j]) such that a[i] * b[j] <= target
    def count(self, a, b, target):
        cnt = 0
        for num in a:
            if num == 0:
                # 0 * any number is 0, which is <= target if target >= 0
                if target >= 0:
                    cnt += len(b)  # All b[j] satisfy the condition

            elif num > 0:
                # For positive num, we need b[j] <= floor(target / num)
                cnt += bisect.bisect_right(b, target // num)

            else:
                # For negative num, we need b[j] >= ceil(target / num)
                # because negative * smaller negative = larger positive
                div = target // num
                if target % num != 0:
                    div += 1  # Apply ceiling manually
                # Count of b[j] >= div is total - number of b[j] < div
                cnt += len(b) - bisect.bisect_left(b, div)
        return cnt

    def kthSmallestProduct(self, a, b, k):
        # Binary search for the k-th smallest product
        # Range: possible min and max values of a[i] * b[j]
        l, r = -10**10, 10**10
        ans = 0
        
        # Binary search to find the smallest value such that
        # there are at least k products <= that value
        while l <= r:
            mid = (l + r) // 2
            if self.count(a, b, mid) >= k:
                ans = mid       # Candidate answer
                r = mid - 1     # Try to find a smaller valid product
            else:
                l = mid + 1     # Increase mid to find at least k products
        return ans
