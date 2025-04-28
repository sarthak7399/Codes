# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

# Example 1:
# Input: nums = [2,1,4,3,5], k = 10
# Output: 6
# Explanation:
# The 6 subarrays having scores less than 10 are:
# - [2] with score 2 * 1 = 2.
# - [1] with score 1 * 1 = 1.
# - [4] with score 4 * 1 = 4.
# - [3] with score 3 * 1 = 3. 
# - [5] with score 5 * 1 = 5.
# - [2,1] with score (2 + 1) * 2 = 6.
# Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)    # Length of the input list
        left = 0         # Left pointer of the sliding window
        total = 0        # Sum of elements inside the window
        count = 0        # Final answer: number of valid subarrays

        for right in range(n):
            total += nums[right]    # Expand window to the right

            # Shrink window from the left while condition is violated
            # Condition: (sum of window elements) * (size of window) must be < k
            while total * (right - left + 1) >= k:
                total -= nums[left] # Remove element at left from total
                left += 1           # Move left pointer right

            # After satisfying the condition, all subarrays ending at 'right' and starting between 'left' and 'right' are valid
            count += (right - left + 1)

        return count
