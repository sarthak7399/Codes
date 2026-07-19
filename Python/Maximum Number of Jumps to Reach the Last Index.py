# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

# Example 2:
# Input: nums = [1,3,6,4,1,2], target = 3
# Output: 5
# Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
# - Jump from index 0 to index 1.
# - Jump from index 1 to index 2.
# - Jump from index 2 to index 3.
# - Jump from index 3 to index 4.
# - Jump from index 4 to index 5.
# It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 5 jumps. Hence, the answer is 5. 

from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # dp[i] = maximum number of jumps needed to reach index i
        # Initialize with -1 (unreachable)
        dp = [-1] * n

        # Starting index requires 0 jumps
        dp[0] = 0

        # Process each index
        for i in range(1, n):

            # Check all previous indices
            for j in range(i - 1, -1, -1):

                # Valid jump if difference is within [-target, target]
                if -target <= nums[i] - nums[j] <= target:

                    # If previous index is reachable
                    if dp[j] > -1:

                        # Update maximum jumps to reach i
                        dp[i] = max(dp[i], dp[j] + 1)

        # Return maximum jumps to reach last index
        # If unreachable, returns -1
        return dp[-1]