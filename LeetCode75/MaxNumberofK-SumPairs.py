# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:
# Input: nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k = 2
# Output: 2

from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums_dict = {}
        for num in nums:
            if k - num in nums_dict and nums_dict[k - num] > 0:
                count += 1
                nums_dict[k - num] -= 1
            else:
                nums_dict[num] = nums_dict.get(num, 0) + 1
        return count