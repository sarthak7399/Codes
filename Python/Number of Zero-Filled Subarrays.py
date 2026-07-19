# https://leetcode.com/problems/number-of-zero-filled-subarrays/

# Example 1:
# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

class Solution:
    def zeroFilledSubarray(self, nums):
        ans = 0          # Stores total count of zero-filled subarrays
        n = len(nums)    # Length of the input array
        curr = 0         # Tracks length of the current consecutive zero streak

        # Iterate through the array
        for i in range(n):
            if nums[i] == 0:
                # Extend the current zero streak
                curr += 1
            else:
                # End of zero streak → add number of subarrays formed
                # Formula: (curr * (curr + 1)) // 2
                # Example: streak of 3 zeros -> [0], [0], [0,0], [0,0,0] → 6
                ans += curr * (curr + 1) // 2
                curr = 0   # Reset streak

        # Handle case where array ends with zeros
        ans += curr * (curr + 1) // 2

        return ans
