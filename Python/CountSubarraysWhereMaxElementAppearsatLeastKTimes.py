# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2024-03-29

# Example 1:
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)  # Find the maximum element in nums
        count = 0  # Initialize the count of subarrays with at least k occurrences of max_element
        temp = {}  # Create a dictionary to store the count of each element in the current window
        left = right = 0  # Initialize the left and right pointers for the window
        
        # Iterate over the nums array
        while right < len(nums):
            if nums[right] in temp:  # Update the count of nums[right] in temp
                temp[nums[right]] += 1
            else:
                temp[nums[right]] = 1
            
            if max_element in temp and temp[max_element] >= k:  # Check if max_element occurs at least k times
                count += len(nums) - right  # Increment count by the length of the current subarray
            
            # Slide the window to the right while maintaining the condition
            while left <= right and max_element in temp and temp[max_element] >= k:
                temp[nums[left]] -= 1  # Update the count of nums[left] in temp
                left += 1
                if temp[max_element] >= k:
                    count += len(nums) - right  # Increment count by the length of the current subarray
            
            right += 1  # Move the right pointer to the next element
        
        return count  # Return the total count of subarrays
