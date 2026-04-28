# https://leetcode.com/problems/minimum-removals-to-balance-array/

# Example 1:
# Input: nums = [2,1,5], k = 2
# Output: 1
# Explanation:
# Remove nums[2] = 5 to get nums = [2, 1].
# Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.

from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Sort the array to enable sliding window
        nums.sort()

        l = 0              # left pointer of the window
        
        maxsize = 0        # size of the largest valid window found

        # Expand the window using right pointer
        for r in range(len(nums)):
            # Shrink window until max/min ratio <= k
            while nums[r] / nums[l] > k:
                l += 1

            # Update maximum valid window size
            maxsize = max(maxsize, r - l + 1)

        # Elements outside the largest valid window must be removed
        return len(nums) - maxsize
