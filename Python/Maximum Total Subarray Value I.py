# https://leetcode.com/problems/maximum-total-subarray-value-i/

# Example 1:
# Input: nums = [1,3,2], k = 2
# Output: 4
# Explanation:
# One optimal approach is:
# Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
# Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.
# Adding these gives 2 + 2 = 4.

from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Track maximum and minimum values in the array
        mx = 0
        mn = float('inf')

        # Find the largest and smallest elements
        for num in nums:

            if num > mx:
                mx = num

            if num < mn:
                mn = num

        # Maximum total value is obtained by taking
        # the difference between max and min, then
        # multiplying it by k
        return (mx - mn) * k