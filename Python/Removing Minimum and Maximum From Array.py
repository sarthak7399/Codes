# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

# Example 1:
# Input: nums = [2,10,7,5,4,1,8,6]
# Output: 5
# Explanation: 
# The minimum element in the array is nums[5], which is 1.
# The maximum element in the array is nums[1], which is 10.
# We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
# This results in 2 + 3 = 5 deletions, which is the minimum number 

class Solution:
    def minimumDeletions(self, nums):
        # Store the length of the array.
        n = len(nums)

        # Find the indices of the minimum and maximum elements.
        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        # left is the earlier index and right is the later index.
        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        # Option 1: Remove both elements from the front.
        # We need to delete up to and including the element at 'right'.
        front = right + 1

        # Option 2: Remove both elements from the back.
        # We need to delete from 'left' through the end.
        back = n - left

        # Option 3: Remove one element from each side.
        # Delete the left element from the front and the right element
        # from the back.
        frontBack = (left + 1) + (n - right)

        # Return the minimum number of deletions among all three options.
        return min(front, back, frontBack)