# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

# Example 3:
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

class Solution:
    def minOperations(self, nums, x):
        # Length of the array.
        n = len(nums)

        # Calculate the total sum of the array.
        total = sum(nums)

        # Instead of removing elements from both ends to get sum x,
        # find the longest subarray whose sum is total - x.
        target = total - x

        # If target is negative, it is impossible to obtain
        # the required sum by keeping a subarray.
        if target < 0:
            return -1

        # If target is 0, all elements must be removed.
        if target == 0:
            return n

        # Left pointer of the sliding window.
        left = 0

        # Current sum of the sliding window.
        s = 0

        # Length of the longest subarray having sum = target.
        longest = -1

        # Expand the window using the right pointer.
        for right in range(n):
            # Add the current element to the window sum.
            s += nums[right]

            # Shrink the window while its sum exceeds the target.
            while left <= right and s > target:
                s -= nums[left]
                left += 1

            # If the current window has the required sum,
            # update the longest valid subarray length.
            if s == target:
                longest = max(longest, right - left + 1)

        # Removing the elements outside the longest valid subarray
        # gives the minimum number of operations.
        return -1 if longest == -1 else n - longest