# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation:
# Select the entire array without deleting any element to obtain the maximum sum.

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum = 0                # To store the sum of unique positive numbers
        st = set()             # Set to store unique positive numbers
        mxNeg = float('-inf')  # Track the maximum (least negative) number if all numbers are non-positive
        
        # Iterate through each number in the list
        for i in range(len(nums)):
            if nums[i] > 0:
                st.add(nums[i])                # Add positive numbers to the set (duplicates automatically handled)
            else:
                mxNeg = max(mxNeg, nums[i])    # Update max negative number if current number is more (less negative)
        
        # Calculate the sum of unique positive numbers
        for val in st:
            sum += val
        
        # If there are positive numbers, return their sum; otherwise, return the maximum negative number
        if len(st) > 0:
            return sum
        else:
            return mxNeg
