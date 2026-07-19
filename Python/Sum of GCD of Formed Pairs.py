# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

# Example 1:
# Input: nums = [2,6,4]
# Output: 2
# Explanation:
# Construct prefixGcd:
# i	nums[i]	mxi	prefixGcd[i]
# 0	2	2	2
# 1	6	6	6
# 2	4	6	2
# prefixGcd = [2, 6, 2]. After sorting, it forms [2, 2, 6].
# Pair the smallest and largest elements: gcd(2, 6) = 2. The remaining middle element 2 is ignored. Thus, the sum is 2.

from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        # Track the maximum value seen so far
        mx = 0

        # Replace each element with the GCD of
        # the current maximum and the element itself
        for i in range(len(nums)):
            mx = max(mx, nums[i])
            nums[i] = gcd(mx, nums[i])

        # Sort the transformed array
        nums.sort()

        # Pair the smallest and largest elements
        left, right = 0, len(nums) - 1
        ans = 0

        while left < right:
            # Add the GCD of the current pair
            ans += gcd(nums[left], nums[right])

            left += 1
            right -= 1

        return ans