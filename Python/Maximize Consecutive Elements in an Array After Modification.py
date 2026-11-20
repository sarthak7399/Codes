# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

# Example 1:
# Input: nums = [2,1,5,1,1]
# Output: 3
# Explanation: We can increase the elements at indices 0 and 3. The resulting array is nums = [3,1,5,2,1].
# We select the elements [3,1,5,2,1] and we sort them to obtain [1,2,3], which are consecutive.
# It can be shown that we cannot select more than 3 consecutive elements.

from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # Sort the array to process elements in increasing order
        nums.sort()

        # dp[x] stores the maximum number of selected elements
        # that can form a consecutive sequence ending at x
        dp = {}

        ans = 0

        # Process each number in sorted order
        for num in nums:

            # Option 1: Increment the current number by 1
            # Extend the sequence ending at num, so it now ends at num + 1
            dp[num + 1] = dp.get(num, 0) + 1

            # Option 2: Keep the current number unchanged
            # Extend the sequence ending at num - 1, so it now ends at num
            dp[num] = dp.get(num - 1, 0) + 1

            # Update the maximum length found so far
            ans = max(ans, dp[num], dp[num + 1])

        # Return the maximum number of elements that can be selected
        return ans