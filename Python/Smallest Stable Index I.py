# https://leetcode.com/problems/smallest-stable-index-i/

# Example 1:
# Input: nums = [5,0,1,4], k = 3
# Output: 3
# Explanation:
# At index 0: The maximum in [5] is 5, and the minimum in [5, 0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
# At index 1: The maximum in [5, 0] is 5, and the minimum in [0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
# At index 2: The maximum in [5, 0, 1] is 5, and the minimum in [1, 4] is 1, so the instability score is 5 - 1 = 4.
# At index 3: The maximum in [5, 0, 1, 4] is 5, and the minimum in [4] is 4, so the instability score is 5 - 4 = 1.
# This is the first index with an instability score less than or equal to k = 3. Thus, the answer is 3.

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # mini[i] stores the minimum value in nums[i:]
        mini = [0] * n

        # Start with infinity so the first element always becomes the minimum.
        mint = float('inf')

        # Build the suffix minimum array from right to left.
        for i in range(n - 1, -1, -1):
            # Update the minimum value seen so far.
            if nums[i] < mint:
                mint = nums[i]

            # Store the minimum value from index i to the end.
            mini[i] = mint

        # maxt stores the maximum value in nums[0:i+1].
        maxt = 0

        # Traverse from left to right to find the first stable index.
        for i in range(n):
            # Update the prefix maximum.
            if nums[i] > maxt:
                maxt = nums[i]

            # The index is stable if the difference between
            # the maximum on the left and minimum on the right
            # is at most k.
            if maxt - mini[i] <= k:
                return i

        # No stable index was found.
        return -1