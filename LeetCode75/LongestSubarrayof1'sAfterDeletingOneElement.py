# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros, ans, n = 0, 0, 0, len(nums)  

        for right in range(n):
            if nums[right] == 0:
                zeros += 1  # Increment the count of zeroes
            while zeros > 1:    # Adjust the window to maintain at most one zero in the subarray
                if nums[left] == 0:
                    zeros -= 1  # Decrement the count of zeroes
                left += 1  # Move the left pointer to the right
            ans = max(ans, right - left + 1 - zeros)  # Calculate the length of the current subarray and update the maximum length
        return ans - 1 if ans == n else ans