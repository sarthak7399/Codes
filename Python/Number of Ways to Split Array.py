# https://leetcode.com/problems/number-of-ways-to-split-array/

# Example 1:
# Input: nums = [10,4,-8,7]
# Output: 2
# Explanation: 
# There are three ways of splitting nums into two non-empty parts:
# - Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
# - Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
# - Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
# Thus, the number of valid splits in nums is 2.

from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Creating a prefix sum array to store the cumulative sum of elements
        prefix = [0]*(len(nums))  # Initialize an array of zeroes with the same length as nums
        prefix[0] = nums[0]  # Set the first element of prefix to the first element of nums

        # Populate the prefix sum array by iterating over the nums list
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]  # Add the current element of nums to the previous sum in the prefix array
        
        count = 0  # Initialize a counter to keep track of valid splits
        
        # Iterate through the array to check where we can split the array
        for i in range(len(nums)-1):  # Loop through each element, excluding the last one
            # Compare the sum of the left part (prefix[i]) with the sum of the right part (total sum - prefix[i])
            if prefix[i] >= prefix[-1] - prefix[i]:
                count += 1  # Increment count if a valid split is found
        
        return count  # Return the total number of valid splits
