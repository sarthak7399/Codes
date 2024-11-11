# https://leetcode.com/problems/prime-subtraction-operation/

# Example 1:
# Input: nums = [4,9,6,10]
# Output: true
# Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
# In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
# After the second operation, nums is sorted in strictly increasing order, so the answer is true.

from bisect import bisect_left
from typing import List
valid = [True] * 1001
valid[0] = valid[1] = False
for i in range(2, len(valid)):
    if valid[i]:
        for j in range(i * i, len(valid), i):
            valid[j] = False
primes = [i for i in range(len(valid)) if valid[i]]

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0
        for num in nums:
            if num <= prev:
                return False
            i = bisect_left(primes, num - prev) - 1
            if i != -1:
                num -= primes[i]
            prev = num
        return True