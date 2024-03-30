# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-15

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

from typing import List
# The algorithm toggles the sign of numbers at indices corresponding to the absolute values of elements in the array, and if a number is encountered again (its index is visited twice), it's added to the result list.
# Method 1 :
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0:
                result.append(num)
            nums[idx] *= -1
        return result
    
# Method 2 :
# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         arr=[0]*(len(nums)+1)
#         for i in nums:
#             arr[i]+=1
#         return[i for i in range(len(arr)) if arr[i]>1]