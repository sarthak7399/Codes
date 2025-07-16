# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

# Example 1:
# Input: nums = [3,1,2,2,2,1,3], k = 2
# Output: 4
# Explanation:
# There are 4 pairs that meet all the requirements:
# - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
# - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
# - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
# - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Create a list of 101 empty lists (since 1 <= nums[i] <= 100)
        # Each index `i` in `freq` will hold the indices where value `i` appears in nums
        freq = [[] for i in range(101)]

        cnt = 0  # Counter for valid pairs

        # Iterate through nums with both index and value
        for j, x in enumerate(nums):
            # For every previous occurrence `i` of the same number `x`
            for i in freq[x]:
                # Check if the product of indices is divisible by k
                if (i * j) % k == 0:
                    cnt += 1
            # Append the current index to the list for number `x`
            freq[x].append(j)

        return cnt
