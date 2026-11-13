# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

# Example 1:
# Input: nums = [6,3,1,2,4,4], k = 7
# Output: 17
# Explanation:
# Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is 21 - 4 = 17.


import collections
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # Stores the total number of valid subarrays.
        ans = 0

        # Stores the number of operations required to make the current
        # sliding window non-decreasing.
        cost = 0

        # Monotonic deque storing (value, count) pairs.
        # It helps efficiently maintain the values needed to calculate the cost.
        dq = collections.deque()

        n = len(nums)

        # Right boundary of the current sliding window.
        j = n - 1

        # Traverse the array from right to left.
        for i in range(n - 1, -1, -1):
            num = nums[i]
            count = 1

            # Merge smaller values from the deque because they need to be
            # increased to the current value to maintain non-decreasing order.
            while dq and dq[-1][0] < num:
                nextNum, nextCount = dq.pop()

                # Combine the number of elements represented by these entries.
                count += nextCount

                # Update the cost of increasing these elements to num.
                cost += (num - nextNum) * nextCount

            # Add the current value and its merged count to the deque.
            dq.append((num, count))

            # Shrink the window from the right while the required operations
            # exceed the allowed budget k.
            while cost > k:
                # Remove the rightmost value represented by the deque's front.
                rightmostNum, rightmostCount = dq.popleft()

                # Remove its contribution to the total operation cost.
                cost -= rightmostNum - nums[j]
                j -= 1

                # If multiple elements were represented by this entry,
                # retain the remaining elements in the deque.
                if rightmostCount > 1:
                    dq.appendleft((rightmostNum, rightmostCount - 1))

            # All subarrays ending at or before j and starting at i
            # are valid, contributing j - i + 1 subarrays.
            ans += j - i + 1

        # Return the total count of valid non-decreasing subarrays.
        return ans