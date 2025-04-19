# https://leetcode.com/problems/count-the-number-of-fair-pairs/

# Example 1:
# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

from bisect import bisect_left, bisect_right
from typing import List

# Method 1: Binary Search - Time Complexity O(NlogN), Space Complexity O(1)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sort the list to allow two-pointer traversal for pair search
        nums.sort()
        count = 0

        # Traverse using two pointers to find valid pairs
        for i in range(len(nums)):
            # Use binary search to find bounds for pairs with nums[i]
            start = bisect_left(nums, lower - nums[i], i + 1)
            end = bisect_right(nums, upper - nums[i], i + 1)
            count += end - start  # Count all valid pairs in this range

        return count


# # Method 2: Brute Force - Time Complexity O(N^2), Space Complexity O(1)
# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         count = flag = 0
#         i, j = 0, len(nums)-1
#         while (i<j):
#             # print(i,j)
#             if (nums[i]+nums[j]>=lower and nums[i]+nums[j]<=upper):
#                 count+=1
#                 # print(i,j)
#             if (i+1 == j):
#                 i+=1
#                 j=len(nums)-1
#             else:
#                 j-=1
#         return count