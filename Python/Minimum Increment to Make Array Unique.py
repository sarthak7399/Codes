# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

# Example 2:
# Input: nums = [3,2,1,2,1,7]
# Output: 6
# Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # nums = [3,2,1,2,1,7]
        #        [1,1,2,2,3,7]

        # mySet = set({ num for num in nums }), 2+4
        nums.sort()
        numTracker = 0
        minIncreament = 0

        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament