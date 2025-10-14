# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

# Example 1:
# Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3
# Output: true
# Explanation:
# The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
# The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
# These two subarrays are adjacent, so the result is true.

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # inc: length of current increasing subarray
        inc = 1
        # prevInc: length of previous increasing subarray before the last break
        prevInc = 0
        # maxLen: stores the maximum possible overlap between consecutive increasing subarrays
        maxLen = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # Continue increasing sequence
                inc += 1
            else:
                # Sequence broke — store the last sequence length
                prevInc = inc
                inc = 1  # reset for the new sequence

            # Calculate maximum combined increasing length seen so far
            # `inc >> 1` means integer division by 2 (a smaller contribution)
            # `min(prevInc, inc)` means overlapping region of two increasing parts
            maxLen = max(maxLen, max(inc >> 1, min(prevInc, inc)))

            # If we found at least 'k' increasing overlap, return True
            if maxLen >= k:
                return True

        # If no such subarrays found
        return False
