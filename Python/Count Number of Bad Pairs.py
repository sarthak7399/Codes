# https://leetcode.com/problems/count-number-of-bad-pairs/

# Example 1:
# Input: nums = [4,1,3,3]
# Output: 5
# Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
# The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
# The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
# The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
# The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
# There are a total of 5 bad pairs, so we return 5.

from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}  # Stores frequency of (num - index) values
        good_pairs = 0  

        for i, num in enumerate(nums):
            key = num - i  # Transform nums[i] to find valid (i, j) pairs
            good_pairs += freq.get(key, 0)  # Count previously seen valid pairs
            freq[key] = freq.get(key, 0) + 1  # Update frequency

        n = len(nums)
        total_pairs = (n * (n - 1)) // 2  # Total possible pairs
        return total_pairs - good_pairs  # Subtract good pairs to get bad pairs
