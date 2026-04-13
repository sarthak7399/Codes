# https://leetcode.com/problems/minimum-distance-to-the-target-element/

# Example 1:
# Input: nums = [1,2,3,4,5], target = 5, start = 3
# Output: 1
# Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        answer = float('inf')  # Initialize with a very large value

        # Traverse the array
        for i in range(len(nums)):
            # Check if current element matches the target
            if nums[i] == target:
                # Update minimum distance from 'start' index
                answer = min(answer, abs(i - start))

        # Return the minimum distance found
        return answer