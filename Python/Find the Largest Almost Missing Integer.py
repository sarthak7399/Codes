# https://leetcode.com/problems/find-the-largest-almost-missing-integer/

# Example 1:
# Input: nums = [3,9,2,1,7], k = 3
# Output: 7
# Explanation:
# 1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
# 2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
# 3 appears in 1 subarray of size 3: [3, 9, 2].
# 7 appears in 1 subarray of size 3: [2, 1, 7].
# 9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
# We return 7 since it is the largest integer that appears in exactly one subarray of size k.

from typing import Counter, List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Store the length of the array.
        n = len(nums)

        # Count the frequency of every number.
        freq = Counter(nums)

        # If k = 1, each subarray contains only one element.
        # Therefore, an element is a valid candidate only if
        # it appears exactly once in the entire array.
        if k == 1:
            candidates = [x for x in freq if freq[x] == 1]

            # Return the largest unique element, or -1 if none exists.
            return max(candidates) if candidates else -1

        # If k equals the entire array length, there is only one
        # possible subarray, containing all elements.
        if k == n:
            return max(nums)

        candidates = []

        # For 1 < k < n, only the first and last elements can
        # potentially appear in exactly one subarray of length k.
        if freq[nums[0]] == 1:
            candidates.append(nums[0])

        if freq[nums[-1]] == 1:
            candidates.append(nums[-1])

        # Return the largest valid candidate, or -1 if none exists.
        return max(candidates) if candidates else -1