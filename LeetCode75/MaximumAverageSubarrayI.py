# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return float('-inf')
        current_sum = sum(nums[:k])  # Initialize the sum of the first k elements
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]  # Slide the window by adding next element and removing first element
            max_sum = max(max_sum, current_sum)    # Update max_sum if the current_sum is greater
        return max_sum / k 
    

# OR
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         max_average = float("-inf")
#         if k > len(nums):
#             return max_average
#         else:
#             current_sum = sum(nums[:k])     # Calculate the initial sum of the first k elements
#             max_average = current_sum / k  # Calculate the average
#             low, high = 0, k
#             while high < len(nums):
#                 current_sum += nums[high] - nums[low]    # Slide the window by adding the next element and subtracting the first element
#                 max_average = max(max_average, current_sum / k)
#                 low += 1
#                 high += 1
#         return max_average