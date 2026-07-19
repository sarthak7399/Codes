# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

# Example 1:
# Input: nums = [1,0,2,1,3]
# Output: [3,3,2,2,1]
# Explanation:
# The maximum possible bitwise OR starting at any index is 3. 
# - Starting at index 0, the shortest subarray that yields it is [1,0,2].
# - Starting at index 1, the shortest subarray that yields the maximum bitwise OR is [0,2,1].
# - Starting at index 2, the shortest subarray that yields the maximum bitwise OR is [2,1].
# - Starting at index 3, the shortest subarray that yields the maximum bitwise OR is [1,3].
# - Starting at index 4, the shortest subarray that yields the maximum bitwise OR is [3].
# Therefore, we return [3,3,2,2,1].

from cmath import inf
from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [inf] * length  # Initialize result array with infinity to store min subarray lengths

        # Traverse the array from left to right
        for i in range(length):
            x = nums[i]       # Current value to combine with previous elements
            res[i] = 1        # The subarray ending at position i always has length at least 1 (itself)
            j = i - 1         # Start looking backwards from previous element

            # Update previous elements' ORs until the OR value stops changing
            while j >= 0 and (nums[j] | x) != nums[j]:
                nums[j] |= x                  # Extend OR to include nums[i]
                res[j] = i - j + 1            # Update length needed for position j
                j -= 1                        # Move further left

        return res
