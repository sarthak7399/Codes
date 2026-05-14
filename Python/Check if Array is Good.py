# https://leetcode.com/problems/check-if-array-is-good/

# Example 1:
# Input: nums = [2, 1, 3]
# Output: false
# Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)  # Largest number in the array

        # A good array must have size = mx + 1
        # Example: [1,2,3,3] → max = 3, length = 4
        if len(nums) != mx + 1:
            return False

        # Frequency array to count occurrences
        freq = [0] * (mx + 1)

        # Count frequency of each number
        for x in nums:

            # Invalid if number is outside valid range [1, mx]
            if x < 1 or x > mx:
                return False

            freq[x] += 1

        # Numbers from 1 to mx-1 must appear exactly once
        for i in range(1, mx):
            if freq[i] != 1:
                return False

        # Largest number (mx) must appear exactly twice
        return freq[mx] == 2