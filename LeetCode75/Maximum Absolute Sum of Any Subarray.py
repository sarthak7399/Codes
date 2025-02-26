# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

# Example 1:
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

class Solution:
    def maxAbsoluteSum(self, nums):
        sum, minSum, maxSum = 0, 0, 0  # Initialize running sum and min/max sums
        
        for num in nums:
            sum += num  # Update running sum
            maxSum = max(maxSum, sum)  # Track maximum prefix sum
            minSum = min(minSum, sum)  # Track minimum prefix sum
        
        return abs(maxSum - minSum)  # Return the maximum absolute sum difference
