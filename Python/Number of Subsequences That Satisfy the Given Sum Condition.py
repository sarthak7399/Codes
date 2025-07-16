# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

# Example 1:
# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7  # To keep results within bounds (required by the problem)

        nums.sort()  # Sort the array to enable two-pointer technique
        n = len(nums)

        # Precompute powers of 2 modulo MOD
        # power[i] = 2^i % MOD → number of subsequences between i elements
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        left, right = 0, n - 1  # Two pointers: one from start, one from end
        ans = 0

        while left <= right:
            # If the smallest + largest <= target, all subsequences between them are valid
            if nums[left] + nums[right] <= target:
                # From left to right: (right - left + 1) elements → 2^(right - left) subsequences
                ans = (ans + power[right - left]) % MOD
                left += 1  # Try with next larger minimum value
            else:
                right -= 1  # Try with smaller maximum value

        return ans
