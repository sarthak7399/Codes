# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

# Example 1:
# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77. 

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n  # Stores max value encountered from the left
        suffix = [0] * n  # Stores max value encountered from the right

        # Populate prefix and suffix arrays
        self.prefix_max(prefix, nums)
        self.suffix_max(suffix, nums)

        ans = 0
        # Iterate through nums to find the maximum triplet value
        for j in range(1, n - 1):
            ans = max(ans, (prefix[j - 1] - nums[j]) * suffix[j + 1])

        return ans

    # Computes the prefix max array
    def prefix_max(self, prefix: List[int], nums: List[int]) -> None:
        max_val = prefix[0] = nums[0]
        for i in range(1, len(nums)):
            max_val = max(max_val, nums[i])
            prefix[i] = max_val

    # Computes the suffix max array
    def suffix_max(self, suffix: List[int], nums: List[int]) -> None:
        max_val = suffix[len(nums) - 1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            max_val = max(max_val, nums[i])
            suffix[i] = max_val
