# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

# Example 1:
# Input: nums = [5,3,2,4]
# Output: 0
# Explanation: We can make at most 3 moves.
# In the first move, change 2 to 3. nums becomes [5,3,3,4].
# In the second move, change 4 to 3. nums becomes [5,3,3,3].
# In the third move, change 5 to 3. nums becomes [3,3,3,3].
# After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.

from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        # Sort the array
        nums.sort()

        # Evaluate the minimum difference possible with at most 3 moves
        min_diff = min(
            nums[n-1] - nums[3],      # Change 3 smallest elements
            nums[n-2] - nums[2],      # Change 2 smallest and 1 largest element
            nums[n-3] - nums[1],      # Change 1 smallest and 2 largest elements
            nums[n-4] - nums[0]       # Change 3 largest elements
        )

        return min_diff