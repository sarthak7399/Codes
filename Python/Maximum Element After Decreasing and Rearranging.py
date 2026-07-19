# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

# Example 2:
# Input: arr = [100,1,1000]
# Output: 3
# Explanation: 
# One possible way to satisfy the conditions is by doing the following:
# 1. Rearrange arr so it becomes [1,100,1000].
# 2. Decrease the value of the second element to 2.
# 3. Decrease the value of the third element to 3.
# Now arr = [1,2,3], which satisfies the conditions.
# The largest element in arr is 3.

from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the array so we can build the sequence greedily
        arr.sort()

        # The next value we would like to place.
        # We start from 1 because the smallest element
        # in the final array must be 1.
        res = 1

        for i in arr:

            # If the current element is large enough,
            # we can make it equal to 'res'
            # (either keep it or decrement it).
            if i >= res:
                res += 1

        # res was incremented one extra time,
        # so the maximum possible element is res - 1
        return res - 1