# https://leetcode.com/problems/minimum-sum-of-squared-difference/

# Example 2:
# Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
# Output: 43
# Explanation: One way to obtain the minimum sum of square difference is: 
# - Increase nums1[0] once.
# - Increase nums2[2] once.
# The minimum of the sum of square difference will be: 
# (2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
# Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.

from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # Store the final sum of squared differences.
        ans = 0

        # Find the maximum absolute difference between corresponding elements.
        maxx = 0

        # Total number of operations available.
        ops = k1 + k2

        for i in range(len(nums1)):
            # Calculate the maximum difference.
            maxx = max(maxx, abs(nums1[i] - nums2[i]))

        # freq[i] stores the number of elements with absolute difference i.
        freq = [0] * (maxx + 1)

        for i in range(len(nums1)):
            # Count the frequency of each absolute difference.
            freq[abs(nums1[i] - nums2[i])] += 1

        # Process differences from largest to smallest.
        # Reduce the largest differences first to minimize the sum of squares.
        for i in range(maxx, 0, -1):
            # Stop when all available operations are used.
            if ops <= 0:
                break

            # Reduce as many differences of size i as possible.
            minn = min(ops, freq[i])

            # Update the remaining operations and frequency counts.
            ops -= minn
            freq[i] -= minn

            # Each reduced difference moves from i to i - 1.
            freq[i - 1] += minn

        # Calculate the sum of squared differences.
        for i in range(maxx, 0, -1):
            ans += i * i * freq[i]

        # Return the minimum possible sum.
        return ans