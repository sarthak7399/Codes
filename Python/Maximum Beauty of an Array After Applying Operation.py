# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

# Example 1:
# Input: nums = [4,6,1,2], k = 2
# Output: 3
# Explanation: In this example, we apply the following operations:
# - Choose index 1, replace it with 4 (from range [4,8]), nums = [4,4,1,2].
# - Choose index 3, replace it with 4 (from range [0,4]), nums = [4,4,1,4].
# After the applied operations, the beauty of the array nums is 3 (subsequence consisting of indices 0, 1, and 3).
# It can be proven that 3 is the maximum possible length we can achieve.

from typing import List
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Sort the list of numbers to efficiently find the maximum beauty
        nums.sort()
        
        # The range width is 2 * k
        range_width = 2 * k
        
        # Initialize the left pointer for the sliding window
        left = 0
        
        # Loop through each number in the sorted list
        for num in nums:
            # If the current number is outside the valid range, move the left pointer
            if nums[left] + range_width < num:
                left += 1
        
        # The result is the number of elements within the range defined by k
        return len(nums) - left