# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/?envType=daily-question&envId=2024-03-31

# Example 1:
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

# Example 2:
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)  # Get the length of the input array
        result = 0  # Initialize the result counter
        minKIndex = -1  # Initialize the index of the last occurrence of minK
        maxKIndex = -1  # Initialize the index of the last occurrence of maxK
        culpritIndex = -1  # Initialize the index of the last element outside the range [minK, maxK]

        # Iterate through the array
        for i in range(n):
            # Check if the current element falls outside the range [minK, maxK]
            if nums[i] < minK or nums[i] > maxK:
                culpritIndex = i  # Update the culprit index to the current index

            # Update the index of the last occurrence of minK
            if nums[i] == minK:
                minKIndex = i

            # Update the index of the last occurrence of maxK
            if nums[i] == maxK:
                maxKIndex = i

            # Determine the smaller index between minKIndex and maxKIndex
            smaller = min(minKIndex, maxKIndex)

            # Calculate the length of the subarray between the culpritIndex and the smaller index
            temp = smaller - culpritIndex

            # Increment the result counter by the length of the valid subarray
            result += temp if temp > 0 else 0

        return result  # Return the total count of valid subarrays
