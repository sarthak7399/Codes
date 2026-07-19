# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

# Example 1:
# Input: nums = [2,5,7,8,9,2,3,4,3,1]
# Output: 3
# Explanation:
# The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
# The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
# These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        l = []          # List to store lengths of strictly increasing subarrays
        start = 0       # Start index of the current increasing subarray

        # Step 1: Split the array into lengths of increasing subarrays
        for i in range(1, len(nums)):
            # If sequence breaks (non-increasing condition)
            if nums[i] <= nums[i - 1]:
                # Store length of current increasing subarray
                l.append(i - start)
                # Start a new subarray from current index
                start = i

        # Step 2: Append the last increasing segment if not already added
        if sum(l) < len(nums):
            l.append(len(nums) - sum(l))

        # Step 3: Initialize result as half of the longest increasing subarray length
        # (Represents max possible overlap inside a single subarray)
        res = max(l) // 2

        # Step 4: Check for maximum overlap between adjacent increasing subarrays
        for i in range(len(l) - 1):
            # The overlap between consecutive subarrays is limited
            # by the smaller of the two lengths (min(l[i], l[i+1]))
            res = max(res, min(l[i], l[i + 1]))

        # Step 5: Return the maximum overlap length found
        return res
