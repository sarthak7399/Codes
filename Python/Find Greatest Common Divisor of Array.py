# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

# Example 1:
# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.

from math import gcd
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # The GCD of the entire array is equal to the GCD
        # of its minimum and maximum values.
        return gcd(min(nums), max(nums))