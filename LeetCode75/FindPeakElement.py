# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)  # Length of the input array
        low, high = 0, n-1  # Initialize pointers for binary search
        while low <= high:
            mid = ((high-low)//2) + low  # Calculate the middle index
            if mid < n-1 and nums[mid] < nums[mid+1]:   # Peak element is present in the right side
                low = mid+1  # Adjust the low pointer to search in the right half   
            elif mid > 0 and nums[mid] < nums[mid-1]:      # Peak element is present in the left side
                high = mid-1  # Adjust the high pointer to search in the left half
            else:
                return mid  # Return the index of the peak element
