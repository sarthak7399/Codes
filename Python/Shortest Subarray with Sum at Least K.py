# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# Example 3:
# Input: nums = [2,-1,2], k = 3
# Output: 3

from collections import deque
from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Initialize prefix sum and deque
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        dq = deque()
        result = float('inf')  # Initialize with infinity (no subarray found)

        # Iterate through the prefix sums
        for i in range(len(prefix_sum)):
            # Check if there's a valid subarray with a sum >= k
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            # Maintain increasing order in the deque for prefix sums
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            # Add the current index to the deque
            dq.append(i)

        # If result is still infinity, no valid subarray was found
        return result if result != float('inf') else -1
