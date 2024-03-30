# https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-15

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

from typing import List
# Method 1 :
# As Sets have constant-time average lookup.O(1).
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1
        while res in nums:
            res += 1        
        return res

# # Method 2 :
# # Cyclic Sort algorithm works efficiently for sorting arrays where the elements are within a limited range. In this case, it is used to find the first missing positive integer in an array.
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         def swap(arr, i, j):    # Function to swap elements in the array
#             arr[i], arr[j] = arr[j], arr[i]        
#         n = len(nums)       
#         for i in range(n):  # Place each positive integer i at index i-1 if possible
#             while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
#                 swap(nums, i, nums[i] - 1)    
#         # Find the first missing positive integer
#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1      
#         return n+1    # If all positive integers from 1 to n are present, return n + 1