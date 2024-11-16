# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

# Example 1:
# Input: nums = [1,2,3,4,3,2,5], k = 3
# Output: [3,4,-1,-1,-1]
# Explanation:
# There are 5 subarrays of nums of size 3:
# [1, 2, 3] with the maximum element 3.
# [2, 3, 4] with the maximum element 4.
# [3, 4, 3] whose elements are not consecutive.
# [4, 3, 2] whose elements are not sorted.
# [3, 2, 5] whose elements are not consecutive.

from typing import List
class Solution:
    def consecutives(self, *args):
        return all(args[i] == args[i-1] + 1 for i in range(1, len(args)))
    
    def sorted(self, *args):
        return all(args[i] < args[i+1] for i in range(len(args)-1))
    
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        i = 0
        res = []
        while i < len(nums) - k + 1 :  # Check for all subarrays
            subarray = nums[i:i+k]
            if self.consecutives(*subarray) and self.sorted(*subarray):
                res.append(nums[i+k-1])  # Append the last element from subarray
            else:
                res.append(-1)  # Append -1 if conditions are not met
            i += 1
        return res