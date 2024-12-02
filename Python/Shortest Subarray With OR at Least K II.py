# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

# Example 1:
# Input: nums = [1,2,3], k = 2
# Output: 1
# Explanation:
# The subarray [3] has OR value of 3. Hence, we return 1.

from typing import List
class Solution:
    def update(self, bits: List[int], x: int, change: int):
        # insert or remove element from window, time: O(32)
        for i in range(32):
            if (x >> i) & 1:
                bits[i] += change

    def bitsToNum(self, bits: List[int]) -> int:
        # convert 32-size bits array to integer, time: O(32)
        result = 0
        for i in range(32):
            if bits[i]:
                result |= 1 << i
        return result
    
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = n + 1
        bits = [0] * 32
        start = 0
        for end in range(n):
            self.update(bits, nums[end], 1) # insert nums[end] into window
            while start <= end and self.bitsToNum(bits) >= k:
                result = min(result, end - start + 1)
                self.update(bits, nums[start], -1) # remove nums[start] from window
                start += 1
        return result if result != n + 1 else -1