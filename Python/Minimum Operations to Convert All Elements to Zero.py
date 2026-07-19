# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

# Example 1:
# Input: nums = [0,2]
# Output: 1
# Explanation:
# Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
# Thus, the minimum number of operations required is 1.

class Solution:
    def minOperations(self, nums):
        stack = [0] * (len(nums) + 1)  # stack to track increasing sequence
        top = 0  # current top index
        ans = 0  # count of operations
        
        for num in nums:
            # remove elements greater than current num
            while stack[top] > num:
                top -= 1
                ans += 1
            # push new number if different from top
            if stack[top] != num:
                top += 1
                stack[top] = num
                
        return ans + top  # total operations = popped + remaining elements
