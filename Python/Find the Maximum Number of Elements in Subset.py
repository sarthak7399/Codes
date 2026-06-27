# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

# Example 1:
# Input: nums = [5,4,1,2,2]
# Output: 3
# Explanation: We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 22 == 4. Hence the answer is 3.

from math import isqrt
from typing import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        # Count the frequency of each number
        freq = Counter(nums)

        # Handle the special case for 1 separately.
        # Since 1² = 1, we can use an odd number of 1's:
        # 1, 3, 5, ...
        res = (freq.pop(1, 0) - 1) | 1

        # Try to build the longest sequence starting from each number
        for f in freq:

            x = f

            # If f itself is a perfect square and its square root
            # appears at least twice, then this value will be handled
            # when processing the smaller number (its root).
            sq = isqrt(x)
            if sq * sq == x and freq.get(sq, 0) > 1:
                continue

            # Length contributed by numbers that can appear twice
            n = 0

            # Keep squaring x while:
            # 1. x is within constraints
            # 2. x appears at least twice
            #
            # We add 2 because such values can be placed symmetrically
            # on both sides of the sequence.
            while x < 31623 and freq.get(x, 0) > 1:
                n += 2
                x *= x

            # If the final x exists at least once,
            # it can be placed in the center (+1),
            # otherwise the sequence ends one element earlier.
            #
            # ((x in freq) << 1) - 1 evaluates to:
            #   1  if x exists
            #  -1  otherwise
            res = max(
                res,
                n + ((x in freq) << 1) - 1
            )

        return res