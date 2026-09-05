# https://leetcode.com/problems/smallest-stable-index-ii/

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
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # ansIdx stores the current index being considered
        # as the first stable index.
        ansIdx = 0

        # globalMax stores the maximum value seen so far
        # while traversing the array.
        globalMax = float('-inf')

        # ansMax stores the maximum value in the prefix
        # ending at the current candidate index.
        ansMax = float('-inf')

        # Traverse the array from left to right.
        for i in range(n):
            # Update the maximum value seen anywhere so far.
            globalMax = max(globalMax, nums[i])

            # Update the candidate prefix maximum only when
            # we reach the current candidate index.
            if i == ansIdx:
                ansMax = max(ansMax, nums[i])

            # If the current value is smaller than the allowed
            # range determined by ansMax and k, the current
            # candidate cannot be a stable index.
            if nums[i] < ansMax - k:
                # Move the candidate to the next index.
                ansIdx = i + 1

                # The maximum for the new candidate prefix is
                # the maximum value encountered so far.
                ansMax = globalMax

        # Return the first valid stable index if one exists.
        # Otherwise, return -1.
        return ansIdx if ansIdx < n else -1