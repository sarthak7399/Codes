# https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-15

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0  # Initialize a counter to keep track of the running sum of 0s and 1s encountered
        max_len = 0  # Initialize a variable to store the maximum length of subarray with equal number of 0s and 1s
        count_map = {0: -1}  # Create a dictionary/map to store the running sum and its corresponding index, only the first occurence of a character is stored

        for i in range(len(nums)):
            if nums[i] == 1:  # If the current element is 1, increment the count
                count += 1
            else:  # If the current element is 0, decrement the count
                count -= 1
            
            if count in count_map:      # Check if the current count exists in the count_map dictionary
                max_len = max(max_len, i - count_map[count])    # If the count exists, update the max_len to the maximum of current max_len and the difference between the current index and the index stored in the count_map
            else:
                count_map[count] = i    # If the count does not exist, add the count as key and the current index as value to the count_map dictionary
        return max_len
