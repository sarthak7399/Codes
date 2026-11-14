# https://leetcode.com/problems/minimum-positive-sum-subarray/

# Example 1:
# Input: nums = [3, -2, 1, 4], l = 2, r = 3
# Output: 1
# Explanation:
# The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:
# [3, -2] with a sum of 1
# [1, 4] with a sum of 5
# [3, -2, 1] with a sum of 2
# [-2, 1, 4] with a sum of 3
# Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # Get the length of the input array.
        n = len(nums)

        # Build a prefix sum array where prefix[i] stores
        # the sum of elements from index 0 to i - 1.
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Initialise the minimum valid positive subarray sum.
        best = float('inf')

        # Consider every possible ending position of a subarray.
        for j in range(l, n + 1):

            # Check all valid subarray lengths between l and r.
            for length in range(l, min(r, j) + 1):

                # Calculate the subarray sum in O(1) using prefix sums.
                s = prefix[j] - prefix[j - length]

                # Update the minimum sum if it is positive and smaller.
                if 0 < s < best:
                    best = s

        # Return -1 if no positive subarray sum within the given length
        # range was found; otherwise, return the minimum sum.
        return -1 if best == float('inf') else best